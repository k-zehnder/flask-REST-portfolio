from .. import db
import datetime
from ..config import key
from typing import Union

class Ranges(db.Model):
    """ Range Model for storing range related details """
    __tablename__ = "ranges"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mountain_range = db.Column(db.String(255),  nullable=False, unique=False)

    peaks = db.relationship('Peaks', backref='ranges', lazy=True)


class Peaks(db.Model):
    """ Peak Model for storing peak related details """
    __tablename__ = "peaks"

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    mountain_peak=db.Column(db.String(255), unique=True, nullable=False)
    elevation_ft=db.Column(db.String(255), nullable=True)
    fourteener=db.Column(db.String(255), nullable=True)
    distance_mi=db.Column(db.Integer, nullable=True)
    elevation_gain_ft=db.Column(db.String(255), nullable=True)
    difficulty=db.Column(db.String(255), nullable=True)
    traffic_low=db.Column(db.Integer, nullable=True)
    traffic_high=db.Column(db.Integer, nullable=True)
    photo=db.Column(db.String(500), nullable=True)

    range_name = db.Column(db.String(255), db.ForeignKey('ranges.mountain_range'))
    reviews = db.relationship('Reviews', backref='peaks', lazy=True)

class Reviews(db.Model):
    __tablename__ = "reviews"

    """ Review Model for storing review related details """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reviewer_name = db.Column(db.String(255), nullable=False, unique=False) # True
    review_text = db.Column(db.String(255), nullable=False)

    review_peak = db.Column(db.String(255), db.ForeignKey('peaks.mountain_peak'))
