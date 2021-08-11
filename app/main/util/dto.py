from flask_restx import Namespace, fields

class PeaksDto:
    api = Namespace('peaks', description='peaks related operations')
    peaks = api.model('peaks', {
        'mountain_peak': fields.String(required=True, description='mountain peak'),
        'elevation_ft': fields.String(required=True, description='elevation_ft'),        
        'fourteener': fields.String(required=True, description='fourteener'),
        'distance_mi': fields.String(required=True, description='distance_mi'),
        'elevation_gain_ft': fields.String(required=True, description='elevation_gain_ft'),
        'difficulty': fields.String(required=True, description='difficulty'),
        'traffic_low': fields.String(required=True, description='traffic_low'),
        'traffic_high': fields.String(required=True, description='traffic_high'),
        'photo': fields.String(required=True, description='photo'),
        
        # foreign key
        'range_name': fields.String(required=True, description='range that mountain peak has relationship with')})

    photo = api.model('photo', {
        'photo': fields.String(required=True, description='photo URL for peak'),
    })

class ReviewsDto:
    api = Namespace('reviews', description='reviews related operations')
    reviews = api.model('reviews', {
        'reviewer_name': fields.String(required=True, description='reviewer name'),
        'review_text': fields.String(required=True, description='review text'),
        'review_peak': fields.String(required=True, description='peak that review is for (e.g. "Castle Peak"')})

    reviews_by_peak = api.model('reviews_by_peak', {
        'reviewer_name': fields.String(required=True, description='all reviews for peak given in GET'),
        'review_text': fields.String(required=True, description='review text'),
        'review_peak': fields.String(required=True, description='reviewed peak')
    })
