from app.main import db
from app.main.model.peak import Peak, Range, Review
from typing import Dict, Tuple

def get_all_peaks():
    return Peak.query.all()

def save_changes(data: Peak) -> None:
    db.session.add(data)
    db.session.commit()

def save_new_review(data):
    wanted_peak_obj = Peak.query.filter_by(mountain_peak=data["mountain_peak"]).first()

    r = Review(
        reviewer_name=data["reviewer_name"],
        review_text=data["review_text"],
        peak_name=wanted_peak_obj.mountain_peak
    )
    db.session.add(r)
    db.session.commit()