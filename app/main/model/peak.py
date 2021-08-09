
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

    range_id = db.Column(db.Integer, db.ForeignKey('range.id'))

# > p1 = Peak(mountain_peak="peak1", range_id=r.id)
# >>> db.session.add(p1)
# >>> db.session.commit()
# >>> 


# >>> from app.main import db
# >>> from app.main.model.peak import Peak, Range
# >>> Range.query.first()
# <Range 1>
# >>> r = Range.query.first()
# >>> r.peaks
# [<Peak 1>]
# >>> for p in r.peaks:
# ...     print(p)
# ... 
# <Peak 1>
# >>> for p in r.peaks:
# ...     print(p.mountain_peak)
# ... 
# peak1
