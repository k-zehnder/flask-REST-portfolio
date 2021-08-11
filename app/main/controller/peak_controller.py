from flask import request
from flask_restx import Resource

from ..util.dto import PeaksDto
from ..service.peak_service import save_changes, get_all_peaks, save_new_review, get_all_reviews
from typing import Dict, Tuple

api = PeaksDto.api
_peaks = PeaksDto.peaks

@api.route('/')
class PeaksList(Resource):
    @api.doc('list_of_all_peaks')
    @api.marshal_list_with(_peaks, envelope='data')
    def get(self):
        """List all peaks"""
        return get_all_peaks()
        

    # @api.expect(_reviews, validate=True)
    # @api.response(201, "Review successfully created.")
    # @api.doc("Create new review.")
    # def post(self):
    #     """Create review for peak"""
    #     data = request.json
    #     return save_new_review(data=data)


