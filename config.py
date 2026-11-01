import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # ---- DATABASE ---------------------------------------------------
    # Default is a local SQLite file. To link YOUR database, set DATABASE_URL:
    #   MySQL:      mysql+pymysql://user:password@host/dbname
    #   PostgreSQL: postgresql+psycopg2://user:password@host/dbname
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "rams.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ---- BUSINESS DETAILS (edit here, used across the whole site) ----
    SITE_URL = os.environ.get("SITE_URL", "https://www.example.co.za").rstrip("/")
    BUSINESS_NAME = "RAMS Digital Solutions"
    TAGLINE = "Creative. Connected. Reliable."
    PHONE_DISPLAY = "+27 71 582 4446"
    PHONE_TEL = "+27715824446"
    WHATSAPP_NUMBER = "27715824446"          # international format, no + or spaces
    EMAIL = "kamogeloramano@icloud.com"
    LOCATION = "South Africa"
