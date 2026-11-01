import json
from urllib.parse import quote

from flask import Flask, render_template, abort, Response, request, url_for

from config import Config
from models import db, Service
from services_data import SERVICES

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


def seed():
    """Load starter services into an empty database."""
    if Service.query.first():
        return
    for i, s in enumerate(SERVICES):
        db.session.add(Service(
            position=i, slug=s["slug"], title=s["title"], icon=s["icon"],
            tagline=s["tagline"], intro=s["intro"],
            groups_json=json.dumps(s["groups"]), faqs_json=json.dumps(s["faqs"]),
            related_json=json.dumps(s["related"])))
    db.session.commit()


with app.app_context():
    db.create_all()
    seed()


def wa_link(text=None):
    base = f"https://wa.me/{app.config['WHATSAPP_NUMBER']}"
    return f"{base}?text={quote(text)}" if text else base


app.jinja_env.globals["wa_link"] = wa_link


@app.context_processor
def inject_globals():
    return dict(
        site=app.config,
        nav_services=Service.query.order_by(Service.position).all(),
        canonical=app.config["SITE_URL"] + request.path,
    )


def seo(title, description):
    return dict(title=title, description=description)


# ------------------------------ pages ----------------------------------
@app.route("/")
def home():
    return render_template(
        "index.html",
        services=Service.query.order_by(Service.position).all(),
        seo=seo("RAMS Digital Solutions | Web Development, IT Support, Networking & CCTV",
                "South African technology company offering graphic design, printing and branding, "
                "website development, IT support, networking and CCTV solutions."))


@app.route("/about")
def about():
    return render_template(
        "about.html",
        seo=seo("About Us | RAMS Digital Solutions",
                "RAMS Digital Solutions is a South African technology company providing reliable, "
                "innovative and affordable IT solutions."))


@app.route("/services")
def services():
    return render_template(
        "services.html",
        services=Service.query.order_by(Service.position).all(),
        seo=seo("Our Services | RAMS Digital Solutions",
                "Graphic design, printing and branding, website development, IT support, "
                "networking and CCTV solutions for South African businesses."))


@app.route("/services/<slug>")
def service_detail(slug):
    svc = Service.query.filter_by(slug=slug).first_or_404()
    related = Service.query.filter(Service.slug.in_(svc.related)).all() if svc.related else []
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": f["q"],
                              "acceptedAnswer": {"@type": "Answer", "text": f["a"]}}
                             for f in svc.faqs]}
    return render_template(
        "service_detail.html", svc=svc, related=related, faq_ld=faq_ld,
        seo=seo(f"{svc.title} | RAMS Digital Solutions", svc.tagline + " " + (svc.intro or "")[:110]))


@app.route("/contact")
def contact():
    return render_template(
        "contact.html",
        seo=seo("Contact Us | RAMS Digital Solutions",
                "Contact RAMS Digital Solutions on WhatsApp, by phone or by email for a quote."))


@app.route("/privacy")
def privacy():
    return render_template("legal.html", kind="privacy",
                           seo=seo("Privacy Policy | RAMS Digital Solutions",
                                   "How RAMS Digital Solutions handles your information."))


@app.route("/terms")
def terms():
    return render_template("legal.html", kind="terms",
                           seo=seo("Terms of Use | RAMS Digital Solutions",
                                   "Terms for using the RAMS Digital Solutions website."))


# ------------------------------ SEO files ------------------------------
@app.route("/robots.txt")
def robots():
    body = f"User-agent: *\nAllow: /\n\nSitemap: {app.config['SITE_URL']}/sitemap.xml\n"
    return Response(body, mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap():
    paths = ["/", "/about", "/services", "/contact", "/privacy", "/terms"]
    paths += [f"/services/{s.slug}" for s in Service.query.order_by(Service.position)]
    urls = "".join(f"<url><loc>{app.config['SITE_URL']}{p}</loc></url>" for p in paths)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    return Response(xml, mimetype="application/xml")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", seo=seo("Page not found | RAMS Digital Solutions",
                                               "The page you were looking for could not be found.")), 404


if __name__ == "__main__":
    app.run(debug=True)
