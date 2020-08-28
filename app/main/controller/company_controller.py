from flask import request
from flask_restx import Resource

from ..util.company_dto import CompanyDto
from ..service.company_service import save_new_company, get_all_companies, get_a_company, delete_company_test_data
api = CompanyDto.api
_company = CompanyDto.company


@api.route('/')
class CompanyList(Resource):
    @api.doc('list_of_companies')
    @api.marshal_list_with(_company, envelope='data')
    def get(self):
        """List all registered companies"""
        return get_all_companies()

    @api.expect(_company, validate=True)
    @api.response(201, 'Company successfully created.')
    @api.doc('create a new Company')
    def post(self):
        """Creates a new Company """
        data = request.json
        return save_new_company(data=data)    


@api.route('/<company_name>')
@api.param('company_name', 'The company identifier')
@api.response(404, 'Company not found.')
class Company(Resource):
    @api.doc('get a company')
    @api.marshal_with(_company)
    def get(self, company_name):
        """get a company given its company name"""
        company = get_a_company(company_name)
        if not company:
            api.abort(404)
        else:
            return company
            
@api.route('/delete/')
class DeleteTestCompany(Resource):
    @api.response(200, 'Company test data successfully deleted')
    @api.doc('delete_company_test_data')
    def get(self):
        """Delete Company Test Data"""
        return delete_company_test_data()
