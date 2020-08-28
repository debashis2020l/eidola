from .. import db, flask_bcrypt
import datetime
from ..config import key
# import jwt
from .. import db

class Customer(db.Model):
    """ Customer Model for storing Customer related details """
    __tablename__ = "customer"

    customer_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    customer_name = db.Column(db.String(50), unique=True)
    diagnostics = db.relationship('DiagnosticData',backref='diag_customer',lazy='dynamic')
    
    def __repr__(self):
        return "<Customer '{}'>".format(self.customer_name)