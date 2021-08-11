from flask import request
from flask_restx import Resource

from ..util.dto import ReviewsDto
from ..service.peak_service import save_changes, get_all_peaks, save_new_review, get_all_reviews, reviews_by_peak
from typing import Dict, Tuple

api = ReviewsDto.api
_reviews = ReviewsDto.reviews
_reviews_by_peak = ReviewsDto.reviews_by_peak

# upload_parser = api.parser()
# upload_parser.add_argument('mountain_peak')

@api.route('/')
class ReviewsList(Resource):
    @api.doc('list_of_all_reviews')
    @api.marshal_list_with(_reviews, envelope='data')
    def get(self):
        """List all reviews"""
        return get_all_reviews()
        

    @api.expect(_reviews, validate=True)
    @api.response(201, "Review successfully created.")
    @api.doc("Create new review.")
    def post(self):
        """Create review for peak"""
        data = request.json
        return save_new_review(data=data)

@api.route('/<mountain_peak>')
class ReviewsByPeak(Resource):
    @api.doc('list_of_all_reviews')
    @api.marshal_list_with(_reviews_by_peak, envelope='data')
    def get(self, mountain_peak):
        """List all reviews"""
        return reviews_by_peak(mountain_peak)