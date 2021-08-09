from flask import request
from flask_restx import Resource

from ..util.dto import PeakDto
from ..service.peak_service import save_changes, get_all_peaks
from typing import Dict, Tuple

api = PeakDto.api
_peak = PeakDto.peak


# PEAKS = get_all_peaks()
# print(f"PEAKS : {PEAKS}")

@api.route('/')
class PeakList(Resource):
    @api.doc('list_of_all_peaks')
    @api.marshal_list_with(_peak, envelope='data')
    def get(self):
        """List all peaks"""
        return get_all_peaks()

    # @api.expect(_user, validate=True)
    # @api.response(201, 'User successfully created.')
    # @api.doc('create a new user')
    # def post(self) -> Tuple[Dict[str, str], int]:
    #     """Creates a new User """
    #     data = request.json
    #     return save_new_user(data=data)


# @api.route('/<public_id>')
# @api.param('public_id', 'The User identifier')
# @api.response(404, 'User not found.')
# class User(Resource):
#     @api.doc('get a user')
#     @api.marshal_with(_user)
#     def get(self, public_id):
#         """get a user given its identifier"""
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             return user



