from .. import db, flask_bcrypt
import datetime
from ..config import key
# import jwt
from .. import db

class Company(db.Model):
    """ Company Model for storing company related details """
    __tablename__ = "company"

    company_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    company_name = db.Column(db.String(50), unique=True)
    diagnostics = db.relationship('DiagnosticData',backref='diag_executor',lazy='dynamic')
    
    def __repr__(self):
        return "<Company '{}'>".format(self.company_name)
