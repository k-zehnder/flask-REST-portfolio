from flask import request
from flask_restx import Resource

from ..util.dto import PeakDto
from ..service.peak_service import save_changes, get_all_peaks, save_new_review
from typing import Dict, Tuple

api = PeakDto.api
_peak = PeakDto.peak
_review = PeakDto.review

@api.route('/')
class PeakList(Resource):
    @api.doc('list_of_all_peaks')
    @api.marshal_list_with(_peak, envelope='data')
    def get(self):
        """List all peaks"""
        return get_all_peaks()
        

    @api.expect(_review, validate=True)
    @api.response(201, "Review successfully created.")
    @api.doc("Create new review.")
    def post(self):
        """Create review for peak"""
        data = request.json
        return save_new_review(data=data)

