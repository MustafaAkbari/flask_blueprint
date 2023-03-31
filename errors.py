from flask import render_template, Blueprint

error_bp = Blueprint("error", __name__)


@error_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template("error_pages/404.html", error=error), 404


@error_bp.app_errorhandler(500)
def page_not_found(error):
    return render_template("error_pages/500.html", error=error), 500
