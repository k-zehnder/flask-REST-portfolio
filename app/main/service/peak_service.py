from app.main import db
from app.main.model.peak import Peak
from typing import Dict, Tuple

def get_all_peaks():
    return Peak.query.all()

def save_changes(data: Peak) -> None:
    db.session.add(data)
    db.session.commit()



