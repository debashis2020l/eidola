from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.company_controller import api as company_ns
from .main.controller.customer_controller import api as customer_ns
from .main.controller.diagnostic_data_controller import api as diagnostic_data_ns
db = main.model.db
blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus (restx) web service'
          )

api.add_namespace(user_ns)
api.add_namespace(company_ns)
api.add_namespace(customer_ns)
api.add_namespace(diagnostic_data_ns)