"""Lambda entry point."""
from flask import Flask, redirect, url_for
from flask_cors import CORS
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
from flask_apispec import use_kwargs, marshal_with  # noqa: F401
from marshmallow import Schema, fields  # noqa: F401


# create app
app = Flask(__name__)
CORS(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title="Serverless API",
        version='1.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
})
docs = FlaskApiSpec(app)
from api import index


@app.route("/")
def main():
    """Index page."""
    return redirect(url_for('api_index', name="mischa"))


docs.register_existing_resources()

if __name__ == "__main__":
    app.run()
