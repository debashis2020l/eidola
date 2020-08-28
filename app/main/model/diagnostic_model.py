from .. import db, flask_bcrypt
import datetime
from ..config import key
# import jwt
from .. import db

class DiagnosticData(db.Model):
    """ DiagnosticData Model for storing DiagnosticData related details """
    __tablename__ = "diagnostic_data"

    diagnostic_id = db.Column(db.Integer, primary_key=True)
    diagnostic_data = db.Column(db.String(16000))
    
    user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    company_id = db.Column(db.Integer,db.ForeignKey('company.company_id'))
    customer_id = db.Column(db.Integer,db.ForeignKey('customer.customer_id'))
    
    
    def __repr__(self):
        return "<DiagnosticData '{}'>".format(self.data)
