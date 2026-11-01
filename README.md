# RAMS Digital Solutions - Flask website (v2)

## Run
    pip install -r requirements.txt
    python app.py          ->  http://127.0.0.1:5000

## Pages
Home, About, Services (+ one page per service), Contact, Privacy, Terms, 404,
plus /sitemap.xml and /robots.txt.

## Edit your business details
All in config.py: phone, WhatsApp number, email, location, tagline.
IMPORTANT: set SITE_URL to your real domain (used for canonical links, sitemap, social previews):
    export SITE_URL="https://yourdomain.co.za"

## Linking your database
Service pages are stored in the `service` table (see models.py), so editing a row changes the site.
Set DATABASE_URL (no code changes):
    MySQL:      pip install PyMySQL         -> mysql+pymysql://user:pass@host/dbname
    PostgreSQL: pip install psycopg2-binary -> postgresql+psycopg2://user:pass@host/dbname
The table is created and filled with starter content on first run (services_data.py).
groups_json / faqs_json / related_json hold JSON text.

## Before going live
- Review all service wording and the placeholder Privacy/Terms text
- Run with a production server: gunicorn app:app
