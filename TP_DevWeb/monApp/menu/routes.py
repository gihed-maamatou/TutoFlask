from flask import current_app, render_template, request

from . import menu_bp


@menu_bp.route("/")
def index():
    return "Hello world !"


@menu_bp.route("/index/")
def index_page():
    name = request.args.get("name", "Cricri")
    return render_template(
        "index.html",
        title="R3.01 Dev Web avec Flask",
        name=name,
    )


@menu_bp.route("/about/")
def about():
    return render_template(
        "about.html",
        title="R3.01 Dev Web avec Flask",
        name=current_app.config["ABOUT"],
    )


@menu_bp.route("/contact/")
def contact():
    return render_template(
        "contact.html",
        title="R3.01 Dev Web avec Flask",
        name=current_app.config["CONTACT"],
    )
