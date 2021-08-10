
from .. import db
import datetime
from ..config import key
from typing import Union

class Range(db.Model):
    """ Range Model for storing range related details """
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

    range_name = db.Column(db.Integer, db.ForeignKey('range.mountain_range'))

    reviews = db.relationship('Review', backref='peak', lazy=True)


class Review(db.Model):
    """ Review Model for storing review related details """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reviewer_name = db.Column(db.String(255), unique=True)
    review_text = db.Column(db.String(255), unique=True)


    peak_name = db.Column(db.Integer, db.ForeignKey('peak.mountain_peak'))
