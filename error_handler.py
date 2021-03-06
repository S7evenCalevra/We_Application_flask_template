from flask import render_template
from main import main

@main.errorhandler(500)
def server_error(err):
    """
    Handle 500 server errors.
    :return {str}: Returns a rendered HTML template as a unicode string.
    """
    return render_template("templates/views/errors/50x.html")


@main.errorhandler(404)
def missing_error(err):
    """
    Handle 404 (missing data) errors.
    :return {str}: Returns a rendered HTML template as a unicode string.
    """
    return render_template("templates/views/errors/404.html")


@main.errorhandler(401)
def unauthorized_error(err):
    """
    Handle 401 (unauthorized) errors.
    :return {str}: Returns a rendered HTML template as a unicode string.
    """
    return render_template("templates/views/errors/401.html")


@main.errorhandler(410)
def expired_error(err):
    """
    Handle 410 (gone) errors.
    :return {str}: Returns a rendered HTML template as a unicode string.
    """
    return render_template("templates/views/errors/410.html")