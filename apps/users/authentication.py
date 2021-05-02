import jwt

from django.conf import settings

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from django.contrib.auth import User


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request, *args, **kwargs):

        if 'Authorization' not in request.headers:
            raise exceptions.AuthenticationFailed('No authorization header')

        jwt_token = request.headers['Authorization']
        try:
            jwt_data = jwt.decode(jwt_token, settings.SECRET_KEY, verify=True)
            user_id = jwt_data['user_id']
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Jwt token has expired')
        except Exception as e:
            raise exceptions.AuthenticationFailed('Incorrect jwt token')

        user = User.objects.get(id=user_id)

        return (user, None)