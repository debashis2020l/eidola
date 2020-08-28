from flask_restx import Namespace, fields

class CustomerDto:
    api = Namespace('customer', description='customer related operations')
    customer = api.model('customer_details', {
        'customer_id': fields.Integer(required=True, description='id of customer'),
        'email': fields.String(required=False, description='The email address'),
        'customer_name': fields.String(required=True, description='The customer name '),
    })
