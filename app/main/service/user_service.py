import uuid
import datetime

from app.main import db
from app.main.model.user_model import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            user_id=data['user_id'],
            email=data['email'],
            user_name=data['user_name']
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.',
        }
        return response_object, 409


def get_all_users():
    return User.query.all()
 
def get_a_user(user_name):
    return User.query.filter_by(user_name=user_name).first()

def delete_user_test_data():
    user_del_data1 = User.query.filter_by(user_id = -999).first()
    user_del_data2 = User.query.filter_by(user_id = -666).first()

    response_object = {
        'status': 'success',
        'message': 'Successfully deleted.',
    }

    if not user_del_data1:
        response_object = {
        'status': 'success',
        'message': 'Test data already deleted.'
        }

    if not user_del_data2:
        response_object = {
        'status': 'success',
        'message': 'Test data already deleted.'
        }

    User.query.filter_by(user_id = -999).delete()
    User.query.filter_by(user_id = -666).delete()
    
    db.session.commit()
    return response_object, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()

