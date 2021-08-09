import uuid
import datetime

from app.main import db
from app.main.model.peak import Peak
from typing import Dict, Tuple

def get_all_peaks():
    return Peak.query.all()

def save_changes(data: Peak) -> None:
    db.session.add(data)
    db.session.commit()

# def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
#     user = User.query.filter_by(email=data['email']).first()
#     if not user:
#         new_user = User(
#             public_id=str(uuid.uuid4()),
#             email=data['email'],
#             username=data['username'],
#             password=data['password'],
#             registered_on=datetime.datetime.utcnow()
#         )
#         save_changes(new_user)
#         return generate_token(new_user)
#     else:
#         response_object = {
#             'status': 'fail',
#             'message': 'User already exists. Please Log in.',
#         }
#         return response_object, 409

# def get_a_user(public_id):
#     return User.query.filter_by(public_id=public_id).first()




