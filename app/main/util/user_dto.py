from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user_details', {
        'user_id': fields.Integer(required=True, description='id of user'),
        'email': fields.String(required=True, description='user email address'),
        'user_name': fields.String(required=True, description='user username'),
    })

