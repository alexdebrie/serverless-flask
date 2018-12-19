from flask_apispec import use_kwargs, marshal_with
from marshmallow import Schema, fields
from app import app
from typing import Optional


class IndexSchema(Schema):
    name: Optional[str] = fields.Str(required=False)


@app.route('/api/', methods=['POST'])
@use_kwargs(IndexSchema(strict=True))
@marshal_with(IndexSchema)
def api_index(name: str = None):
    """Main API endpoint."""
    return {'name': f'you entered {name}'}
