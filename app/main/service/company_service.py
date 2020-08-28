import uuid
import datetime

from app.main import db
from app.main.model.company_model import Company


def save_new_company(data):
    company = Company.query.filter_by(email=data['email']).first()
    if not company:
        new_company = Company(
            company_id=data['company_id'],
            email=data['email'],
            company_name=data['company_name']
        )
        save_changes(new_company)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Company already exists.',
        }
        return response_object, 409


def get_all_companies():
    return Company.query.all()


def get_a_company(company_name):
    return Company.query.filter_by(company_name=company_name).first()

def delete_company_test_data():
    company_del_data1 = Company.query.filter_by(company_id = -888).first()
    company_del_data2 = Company.query.filter_by(company_id = -555).first()

    response_object = {
        'status': 'success',
        'message': 'Successfully deleted.',
    }

    if not company_del_data1:
        response_object = {
        'status': 'success',
        'message': 'Test data already deleted.'
        }

    if not company_del_data2:
        response_object = {
        'status': 'success',
        'message': 'Test data already deleted.'
        }

    Company.query.filter_by(company_id = -888).delete()
    Company.query.filter_by(company_id = -555).delete()
    
    db.session.commit()
    return response_object, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()

