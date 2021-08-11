
from .. import db
import datetime
from ..config import key
from typing import Union

class Ranges(db.Model):
    """ Range Model for storing range related details """
    __tablename__ = "ranges"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mountain_range = db.Column(db.String(255),  nullable=False, unique=True)

    peaks = db.relationship('Peaks', backref='ranges', lazy=True)


class Peaks(db.Model):
    """ Peak Model for storing peak related details """
    __tablename__ = "peaks"

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

    range_name = db.Column(db.String(255), db.ForeignKey('ranges.mountain_range'))

    reviews = db.relationship('Reviews', backref='peaks', lazy=True)


class Reviews(db.Model):
    __tablename__ = "reviews"

    """ Review Model for storing review related details """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reviewer_name = db.Column(db.String(255), nullable=False, unique=True)
    review_text = db.Column(db.String(255), nullable=False)

    review_peak = db.Column(db.String(255), db.ForeignKey('peaks.mountain_peak'))
