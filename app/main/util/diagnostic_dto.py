from flask_restx import Namespace, fields

class DiagnosticDto:
    api = Namespace('diagnostic_data', description='Diagnostic related operations')
    diagnostic_data = api.model('diagnostic_data_details', {
        'diagnostic_id': fields.Integer(required=True, description='id of diagnostic'),
        'diagnostic_data': fields.String(required=True, description='diagnostic data '),
        'user_id': fields.Integer(required=True, description='The user id '),
        'company_id': fields.Integer(required=True, description='The company id '),
        'customer_id': fields.Integer(required=True, description='The customer id '),
    })