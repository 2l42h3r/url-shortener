import string
from core.models import ShortUrlTable
from core import app, db
from random import choice

from flask import jsonify, request, redirect


def generate_shortened(length: int) -> str:
    return "".join(choice(string.ascii_letters + string.digits) for _ in range(length))


@app.route("/", methods=["POST"])
def index():
    url = request.json["url"]

    if url is None:
        return "URL can't be null", 400

    if not (url.startswith("http://") or url.startswith("https://")):
        return "Not a valid URL", 400

    shortened = generate_shortened(5)

    new_link = ShortUrlTable(full_url=url, shortened=shortened)

    db.session.add(new_link)
    db.session.commit()

    return jsonify(shortened=shortened)


@app.route("/<shortened>")
def redirect_url(shortened: str):
    link = ShortUrlTable.query.filter_by(shortened=shortened).first()

    if link:
        return redirect(link.full_url)

    return "Invalid URL", 404
