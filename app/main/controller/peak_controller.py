from flask import request
from flask_restx import Resource

from ..util.dto import PeaksDto
from ..service.peak_service import save_changes, get_all_peaks, save_new_review, get_all_reviews, get_photo
from typing import Dict, Tuple

api = PeaksDto.api
_peaks = PeaksDto.peaks
_photo = PeaksDto.photo

@api.route('/')
class PeaksList(Resource):
    @api.doc('list_of_all_peaks')
    @api.marshal_list_with(_peaks, envelope='data')
    def get(self):
        """List all peaks"""
        return get_all_peaks()
        
@api.route('/<mountain_peak>')
class PhotosList(Resource):
    @api.doc('peak_photo')
    @api.marshal_list_with(_photo, envelope='data')
    def get(self, mountain_peak):
        """List all photos"""
        return get_photo(mountain_peak)
        


