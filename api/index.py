from flask_apispec import use_kwargs, marshal_with
from marshmallow import Schema, fields
from app import app


class IndexSchema(Schema):
    name = fields.Str(required=False)


@app.route('/api/', methods=['POST'])
@use_kwargs(IndexSchema)
@marshal_with(IndexSchema)
def api_index(name: str = None):
    """Main API endpoint."""
    return {'name': f'you entered {name}'}
