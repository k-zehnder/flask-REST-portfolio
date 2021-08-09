
from .. import db
import datetime
from ..config import key
from typing import Union

class Peak(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "peak"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mountain_peak = db.Column(db.String(255), unique=True, nullable=False)
    mountain_range = db.Column(db.String(255), nullable=False)

