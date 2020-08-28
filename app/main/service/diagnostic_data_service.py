import uuid
import datetime

from app.main import db
from app.main.model.diagnostic_model import DiagnosticData


def save_new_diagnostic_data(data):
    diagnostic_data = DiagnosticData.query.filter_by(diagnostic_data=data['diagnostic_data']).first()
    if not diagnostic_data:
        new_diagnostic_data = DiagnosticData(
            diagnostic_id=data['diagnostic_id'],
            diagnostic_data=data['diagnostic_data'],
            user_id=data['user_id'],
            company_id=data['company_id'],
            customer_id=data['customer_id']
        )
        save_changes(new_diagnostic_data)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Diagnostic Data already exists.',
        }
        return response_object, 409


def get_all_diagnostic_data():
    return DiagnosticData.query.all()


def get_a_diagnostic_data(diagnostic_id):
    return DiagnosticData.query.filter_by(diagnostic_id=diagnostic_id).first()

def delete_diagnostic_test_data():
    diagnostic_del_data1 = DiagnosticData.query.filter_by(diagnostic_id = -333).first()
    diagnostic_del_data2 = DiagnosticData.query.filter_by(diagnostic_id = -222).first()

    response_object = {
        'status': 'success',
        'message': 'Successfully deleted.',
    }

    if not diagnostic_del_data1:
        response_object = {
        'status': 'success',
        'message': 'Test data already deleted.'
        }

    if not diagnostic_del_data2:
        response_object = {
        'status': 'success',
        'message': 'Test data already deleted.'
        }

    DiagnosticData.query.filter_by(diagnostic_id = -222).delete()
    DiagnosticData.query.filter_by(diagnostic_id = -333).delete()

 
    db.session.commit()
    return response_object, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()

