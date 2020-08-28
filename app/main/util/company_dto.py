from flask_restx import Namespace, fields

class CompanyDto:
    api = Namespace('company', description='company related operations')
    company = api.model('company_details', {
        'company_id': fields.Integer(required=True, description='id of company'),
        'email': fields.String(required=True, description='The email address'),
        'company_name': fields.String(required=True, description='The company name '),
    })

