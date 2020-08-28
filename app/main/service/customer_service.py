import uuid
import datetime

from app.main import db
from app.main.model.customer_model import Customer


def save_new_customer(data):
    customer = Customer.query.filter_by(email=data['email']).first()
    if not customer:
        new_customer = Customer(
            customer_id=data['customer_id'],
            email=data['email'],
            customer_name=data['customer_name']
        )
        save_changes(new_customer)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Customer already exists.',
        }
        return response_object, 409


def get_all_customers():
    return Customer.query.all()


def get_a_customer(customer_name):
    return Customer.query.filter_by(customer_name=customer_name).first()

def delete_customer_test_data():
    customer_del_data1 = Customer.query.filter_by(customer_id = -777).first()
    customer_del_data2 = Customer.query.filter_by(customer_id = -444).first()

    response_object = {
        'status': 'success',
        'message': 'Successfully deleted.',
    }

    if not customer_del_data1:
        response_object = {
        'status': 'success',
        'message': 'Test data already deleted.'
        }

    if not customer_del_data2:
        response_object = {
        'status': 'success',
        'message': 'Test data already deleted.'
        }

    Customer.query.filter_by(customer_id = -777).delete()
    Customer.query.filter_by(customer_id = -444).delete()
    
    db.session.commit()
    return response_object, 200
def save_changes(data):
    db.session.add(data)
    db.session.commit()

