from flask_restx import Namespace, fields

class PeaksDto:
    api = Namespace('peaks', description='peaks related operations')
    peaks = api.model('peaks', {
        'mountain_peak': fields.String(required=True, description='mountain peak name'),
        'range_name': fields.String(required=True, description='range that mountain peak has relationship with')
    })

    # reviews = api.model('reviews', {
    #     'reviewer_name': fields.String(required=True, description='reviewer name'),
    #     'review_text': fields.String(required=True, description='review text'),
    #     'review_peak': fields.String(required=True, description='peak that review is for (e.g. "Castle Peak"')
    # })


class ReviewsDto:
    api = Namespace('reviews', description='reviews related operations')
    reviews = api.model('reviews', {
        'reviewer_name': fields.String(required=True, description='reviewer name'),
        'review_text': fields.String(required=True, description='review text'),
        'review_peak': fields.String(required=True, description='peak that review is for (e.g. "Castle Peak"')
    })
