from flask import request
from flask_restx import Resource

from ..util.diagnostic_dto import DiagnosticDto
from ..service.diagnostic_data_service import save_new_diagnostic_data, get_all_diagnostic_data, get_a_diagnostic_data, delete_diagnostic_test_data
api = DiagnosticDto.api
_diagnostic_data = DiagnosticDto.diagnostic_data


@api.route('/')
class DiagnosticDataList(Resource):
    @api.doc('list_of_diagnostic_data')
    @api.marshal_list_with(_diagnostic_data, envelope='data')

    def get(self):
        """List all Diagnostic data"""
        return get_all_diagnostic_data()

    @api.expect(_diagnostic_data, validate=True)
    @api.response(201, 'Diagnostic Data successfully created.')
    @api.doc('create a new Diagnostic Data')
    def post(self):
        """Creates a new Diagnostic Data"""
        data = request.json
        return save_new_diagnostic_data(data=data)    


@api.route('/<diagnostic_id>')
@api.param('diagnostic_id', 'The diagnostic_data identifier')
@api.response(404, 'Diagnostic Data not found.')
class DiagnosticData(Resource):
    @api.doc('get a diagnostic data')
    @api.marshal_with(_diagnostic_data)
    def get(self, diagnostic_id):
        """get a Diagnostic Data given its Diagnostic Data"""
        diagnostic_data= get_a_diagnostic_data(diagnostic_id)
        if not diagnostic_data:
            api.abort(404)
        else:
            return diagnostic_data
@api.route('/delete/')
class DeleteTestDiagnostic(Resource):
    @api.response(200, 'Diagnostic test data successfully deleted')
    @api.doc('delete_diagnostic_test_data')
    def get(self):
        """Delete Diagnostic Test Data"""
        return delete_diagnostic_test_data()