from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django.conf import settings
from django.contrib import auth
import jwt
from rest_framework import status
import bcrypt

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

        user = auth.authenticate(email=email, password=login_password)

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
