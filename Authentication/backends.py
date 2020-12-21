
import jwt
from rest_framework import authentication
from django.conf import settings
from .models import Account

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        prefix, token.auth_data.decode('utf-8').split(' ')

        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            user = Account.objects.get(username=payload['username'])
            return (Account, token)

        except jwt.DecodeError as identifier:
            raise exceptions.authenticationFailed('Login token is invalid')

        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.authenticationFailed('Login token has expired')

        return super().authenticate(request)