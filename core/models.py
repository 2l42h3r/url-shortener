from core import db


class ShortUrlTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_url = db.Column(db.String(500), nullable=False)
    shortened = db.Column(db.String(10), nullable=False, unique=True)
