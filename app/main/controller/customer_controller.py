from flask import request
from flask_restx import Resource

from ..util.customer_dto import CustomerDto
from ..service.customer_service import save_new_customer, get_all_customers, get_a_customer, delete_customer_test_data
api = CustomerDto.api
_customer = CustomerDto.customer


@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_customers')
    @api.marshal_list_with(_customer, envelope='data')

    def get(self):
        """List all registered customers"""
        return get_all_customers()

    @api.expect(_customer, validate=True)
    @api.response(201, 'Customer successfully created.')
    @api.doc('create a new Customer')
    def post(self):
        """Creates a new Customer """
        data = request.json
        return save_new_customer(data=data)    


@api.route('/<customer_name>')
@api.param('customer_name', 'The customer identifier')
@api.response(404, 'customer not found.')
class Customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_customer)
    def get(self, customer_name):
        """get a customer given its customer name"""
        customer = get_a_customer(customer_name)
        if not customer:
            api.abort(404)
        else:
            return customer
@api.route('/delete/')
class DeleteTestCustomer(Resource):
    @api.response(200, 'Customer test data successfully deleted')
    @api.doc('delete_customer_test_data')
    def get(self):
        """Delete Customer Test Data"""
        return delete_customer_test_data()