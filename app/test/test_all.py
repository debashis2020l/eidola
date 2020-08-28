import unittest
from app.main import db
# from app.main.model.blacklist import BlacklistToken
import json
from app.test.base import BaseTestCase


def delete_test_user(self):
    return self.client.get(
        '/user/delete/',
        content_type='application/json'
    )

def delete_test_company(self):
    return self.client.get(
        '/company/delete/',
        content_type='application/json'
    )
def delete_test_customer(self):
    return self.client.get(
        '/customer/delete/',
        content_type='application/json'
    )
def delete_test_diagnostic(self):
    return self.client.get(
        '/diagnostic_data/delete/',
        content_type='application/json'
    )

##################################################################################

def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            user_id=-999,
            email='steve@gmail.com',
            user_name='steve'
        )),
        content_type='application/json'
    )

def register_new_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            user_id=-666,
            email='steve1@gmail.com',
            user_name='steve1'
        )),
        content_type='application/json'
    )

def register_company(self):
    return self.client.post(
        '/company/',
        data=json.dumps(dict(
            company_id=-888,
            email='admin@google.com',
            company_name='google'
        )),
        content_type='application/json'
    )

def register_new_company(self):
    return self.client.post(
        '/company/',
        data=json.dumps(dict(
            company_id=-555,
            email='admin1@google.com',
            company_name='google1'
        )),
        content_type='application/json'
    )


def register_customer(self):
    return self.client.post(
        '/customer/',
        data=json.dumps(dict(
            customer_id=-777,
            email='john@gmail.com',
            customer_name='john'
        )),
        content_type='application/json'
    )
def register_new_customer(self):
    return self.client.post(
        '/customer/',
        data=json.dumps(dict(
            customer_id=-444,
            email='joh1n@gmail.com',
            customer_name='joh1n'
        )),
        content_type='application/json'
    )


def register_diagnostic(self):
    return self.client.post(
        '/diagnostic_data/',
        data=json.dumps(dict(
            diagnostic_id=-333,
            diagnostic_data='some_data',
            user_id=-999,
            company_id=-888,
            customer_id=-777
        )),
        content_type='application/json'
    )
def register_new_diagnostic(self):
    return self.client.post(
        '/diagnostic_data/',
        data=json.dumps(dict(
            diagnostic_id=-222,
            diagnostic_data='some_new_data',
            user_id=-666,
            company_id=-555,
            customer_id=-444
        )),
        content_type='application/json'
    )


class TestAuthBlueprint(BaseTestCase):
    
    def test_adeletion_user(self):
        """ User Deleteion """
        with self.client:
            response = delete_test_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully deleted.' or 'Test data already deleted.')
            # self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)
    
    def test_adeletion_company(self):
        """ Company Deleteion """
        with self.client:
            response = delete_test_company(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully deleted.' or 'Test data already deleted.')
            # self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_adeletion_customer(self):
        """ Customer Deleteion """
        with self.client:
            response = delete_test_customer(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully deleted.' or 'Test data already deleted.')
            # self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_adeletion_adignostic(self):
        """ Diagnostic Data Deleteion """
        with self.client:
            response = delete_test_diagnostic(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully deleted.' or 'Test data already deleted.')
            # self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

####################################################################################
    
    def test_creation_user(self):
        """ User Registration """
        with self.client:
            response = register_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            # self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_creation_company(self):
        """ Company Registration """
        with self.client:
            response = register_company(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            # # self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_creation_customer(self):
        """ Customer Registration """
        with self.client:
            response = register_customer(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            # self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_creation_zdiagnostic(self):
        """ Diagnostic Data Registration """
        with self.client:
            response = register_diagnostic(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            # self.assertTrue(data['Authorization'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)


###################################################################################

            
    def test_registered_with_already_registered_user(self):
        """ User Creation with already registered email"""
        register_new_user(self)
        with self.client:
            response = register_new_user(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'User already exists.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

    def test_registered_with_already_registered_comapny(self):
        """ Company Creation with already registered email"""
        register_new_company(self)
        with self.client:
            response = register_new_company(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Company already exists.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)       
    
    def test_registered_with_already_registered_customer(self):
        """ Customer Creation with already registered email"""
        register_new_customer(self)
        with self.client:
            response = register_new_customer(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Customer already exists.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)
 
    def test_registered_with_already_registered_zdiagnostic(self):
        """ Diagnostic data Creation with already registered email"""
        register_new_diagnostic(self)
        with self.client:
            response = register_new_diagnostic(self)
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Diagnostic Data already exists.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 409)

if __name__ == '__main__':
    unittest.main()
