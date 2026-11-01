import json
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Service(db.Model):
    """One row per service page. Edit these rows in your database to
    change the website - no code changes needed."""
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.Integer, default=0)
    slug = db.Column(db.String(60), unique=True, nullable=False)
    title = db.Column(db.String(120), nullable=False)
    icon = db.Column(db.String(30), default="web")
    tagline = db.Column(db.String(200))          # short line for cards
    intro = db.Column(db.Text)                   # paragraph under the page title
    groups_json = db.Column(db.Text, default="[]")   # [{title, blurb, items:[{name, desc}]}]
    faqs_json = db.Column(db.Text, default="[]")     # [{q, a}]
    related_json = db.Column(db.Text, default="[]")  # [slug, ...]

    @property
    def groups(self): return json.loads(self.groups_json or "[]")
    @property
    def faqs(self): return json.loads(self.faqs_json or "[]")
    @property
    def related(self): return json.loads(self.related_json or "[]")
