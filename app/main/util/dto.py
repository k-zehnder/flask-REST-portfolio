from flask_restx import Namespace, fields


# class UserDto:
#     api = Namespace('user', description='user related operations')
#     user = api.model('user', {
#         'email': fields.String(required=True, description='user email address'),
#         'username': fields.String(required=True, description='user username'),
#         'password': fields.String(required=True, description='user password'),
#         'public_id': fields.String(description='user Identifier')
#     })


class PeakDto:
    api = Namespace('peak', description='peak related operations')
    peak = api.model('peak', {
        'mountain_peak': fields.String(required=True, description='mountain peak name'),
        'mountain_range': fields.String(required=True, description='range that mountain peak resides on')
    })
