"""Lambda entry point."""
from flask import Flask, redirect, url_for
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix
from api.doc import ServerlessOpenAPI

# create app
app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
docs = ServerlessOpenAPI(app)

# set up views
import api.index
docs.register_all()


@app.route("/")
def main():
    """Index page."""
    return redirect(url_for('flask-apispec.swagger-ui'))


if __name__ == "__main__":
    app.run()
