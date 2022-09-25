from flask import Blueprint
from http import HTTPStatus
from flasgger import swag_from


user_api = Blueprint('api',__name__)

@user_api.route('/user/login')

@swag_from({
    'response':{
        HTTPStatus.OK.value:{
            'description': 'User Login',
            
        }
    }
})

def login():
    return {"token":"test"}