
from .. import db, flask_bcrypt
import datetime
from ..config import key

from .. import db
# import jwt

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    user_name = db.Column(db.String(50), unique=True)
    diagnostics = db.relationship('DiagnosticData',backref='diag_user',lazy='dynamic')
    
    def __repr__(self):
        return "<User '{}'>".format(self.user_name)
