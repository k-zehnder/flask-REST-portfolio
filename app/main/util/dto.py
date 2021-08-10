from flask_restx import Namespace, fields

class PeakDto:
    api = Namespace('peak', description='peak related operations')
    peak = api.model('peak', {
        'mountain_peak': fields.String(required=True, description='mountain peak name'),
        'range_name': fields.String(required=True, description='range that mountain peak has relationship with')
    })

    review = api.model('review', {
        'reviewer_name': fields.String(required=True, description='reviewer name'),
        'review_text': fields.String(required=True, description='review text')
    })
