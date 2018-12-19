"""Generate OpenAPI documentation."""
from flask import Flask
from flask_apispec.extension import FlaskApiSpec, make_apispec


class ServerlessOpenAPI:
    def __init__(self, app: Flask) -> None:
        app.config.update({
            'APISPEC_SPEC': make_apispec(title='Flask API', version='v1'),
            'APISPEC_SWAGGER_URL': '/swagger/',
        })
        self.apispec = FlaskApiSpec(app)

    def register_all(self):
        """Generate documentation.

        Call after all views loaded.
        """
        self.apispec.register_existing_resources()


# lambda function
def get_openapi(event, context):
    """Get raw OpenAPI v2 API description."""
    from app import docs
    return docs.apispec.spec.to_dict()
