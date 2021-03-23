from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, ResetPasswordSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework import status
import bcrypt
from .util import Util
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .models import  Account

# Create your views here.

@permission_classes((permissions.AllowAny,))
class RegisterUser(APIView):

    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        
        user = request.data
        serializers = self.serializer_class(data=user)

        if serializers.is_valid(raise_exception=True):

            serializers.save()

            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class LoginUser(APIView):

    def post(self, request):

        data = request.data

        email = data.get('email','')
        password = data.get('password','')

        user = auth.authenticate(email=email, password=password)

        if user:
            auth_token = jwt.encode(
                {
                    'username':user.email
                }, settings.JWT_SECRET_KEY
            )

            serializer = RegisterSerializer(user)

            data = {
                'user': serializer.data, 'token':auth_token
            }
            return Response(
                data, status=status.HTTP_200_OK
                )
        return Response({'detail':'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST,)


@permission_classes((permissions.AllowAny,))
class ResetPassword(APIView):
    
    serializer_class = ResetPasswordSerializer
    
    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)        
        email = request.data['email']
        
        if Account.objects.filter(email=email).exists:
            user                = Account.objects.get(email=email)
            user_id_encode      = urlsafe_base64_encode( smart_bytes(user.id))
            token               = PasswordResetTokenGenerator().make_token(user)
            
            current_site        = get_current_site(request=request).domain
            reversal_link       = reverse('reset-password', kwargs={'user_id_encode':user_id_encode, 'token':token})
            the_url             = 'http://' + current_site + reversal_link
            email_body          = 'Hi '+ user.first_name +' '+ user.last_name +' use the link below to change your password \n'  + the_url
            data                = {'email_body':email_body, 'to_email':user.email, 'email_subject':'Change account password'}
            
            
            Util.send_email(data)
            
        return Response({'success':'We have sent you the link to change your password in your email'}, status=status.HTTP_200_OK)

class PasswordTokenCheck(APIView):
    
    def get(self, request, user_id_encode, token):
        
        try:
            
            user_id = 
            
        except :
            pass
        
