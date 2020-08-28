from flask import request
from flask_restx import Resource

# from app.main.util.decorator import admin_token_required
from ..util.user_dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, delete_user_test_data

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    # @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<user_name>')
@api.param('user_name', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, user_name):
        """get a user given its identifier"""
        user = get_a_user(user_name)
        if not user:
            api.abort(404)
        else:
            return user
@api.route('/delete/')
class DeleteTestUser(Resource):
    @api.response(200, 'User test data successfully deleted')
    @api.doc('delete_user_test_data')
    def get(self):
        """Delete User Test Data"""
        return delete_user_test_data()


