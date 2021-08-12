from app.main import db
from app.main.model.peaks import Peaks, Ranges, Reviews
from typing import Dict, Tuple

def get_all_peaks():
    return Peaks.query.all()

def get_all_reviews():
    print(f"type: {Reviews.query.all()}")
    return Reviews.query.all()

def reviews_by_peak(peak):
    return Reviews.query.filter_by(review_peak=peak).all()

def get_photo(peak):
    return Peaks.query.filter_by(mountain_peak=peak).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def save_new_review(data):
    wanted_peak_obj = Peaks.query.filter_by(mountain_peak=data["review_peak"]).first()
    print(f"wanted peak obj: {wanted_peak_obj.mountain_peak}")

    r = Reviews(
        reviewer_name=data["reviewer_name"],
        review_text=data["review_text"],
        review_peak=wanted_peak_obj.mountain_peak
    )
    db.session.add(r)
    db.session.commit()

    name  = data["reviewer_name"]
    text = data["review_text"]
    peak_name = data["review_peak"]

    print(f"reviewer name: {name}")
    print(f"reviewer text: {text}")
    print(f"reviewer mtn: {peak_name}")

    response_object = {
        "status": "success",
        "message": f"Successfully entered review for reviewer.",
    }
    return response_object, 201