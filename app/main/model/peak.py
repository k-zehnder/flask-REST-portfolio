
from .. import db
import datetime
from ..config import key
from typing import Union

class Range(db.Model):
    __tablename__ = "range"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mountain_range = db.Column(db.String(255), unique=True, nullable=False)

    peaks = db.relationship('Peak', backref='range', lazy=True)


class Peak(db.Model):
    """ Peak Model for storing peak related details """
    __tablename__ = "peak"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mountain_peak = db.Column(db.String(255), unique=True, nullable=False)
    # elevation_ft=
    # fourteener=
    # distance_mi=
    # elevation_gain_ft=
    # difficulty=
    # traffic_low=
    # traffic_high=
    # photo=

    # range_id = db.Column(db.Integer, db.ForeignKey('range.id'))
    range_name = db.Column(db.Integer, db.ForeignKey('range.mountain_range'))
