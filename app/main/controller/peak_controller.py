from flask import request
from flask_restx import Resource

from ..util.dto import PeakDto
from ..service.peak_service import save_changes, get_all_peaks
from typing import Dict, Tuple

api = PeakDto.api
_peak = PeakDto.peak

@api.route('/')
class PeakList(Resource):
    @api.doc('list_of_all_peaks')
    @api.marshal_list_with(_peak, envelope='data')
    def get(self):
        """List all peaks"""
        return get_all_peaks()






