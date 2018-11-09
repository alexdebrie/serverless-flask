"""Lambda entry point."""
from flask import Flask, redirect, url_for
from flask_cors import CORS
from flask_apispec.extension import FlaskApiSpec, make_apispec
from flask_apispec import use_kwargs, marshal_with  # noqa: F401
from marshmallow import Schema, fields  # noqa: F401


# create app
app = Flask(__name__)
CORS(app)
app.config.update({
    'APISPEC_SPEC': make_apispec(title='Flask API', version='v1'),
    'APISPEC_SWAGGER_URL': '/swagger/',
})
docs = FlaskApiSpec(app)

# set up views
import api.index


@app.route("/")
def main():
    """Index page."""
    return redirect(url_for('flask-apispec.swagger-ui'))


docs.register_existing_resources()

if __name__ == "__main__":
    app.run()
