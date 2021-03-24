from rest_framework import serializers
from .models import Account
from rest_framework.validators import UniqueValidator
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField( max_length=280, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password' ]
        
    def validate(self, attrs):
        email = attrs.get('email', '')
        if Account.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email',('email is already in use')})
        send_mail(
            'WELCOME TO HOME MARVENS',
            'Home Mavens is a site where home-seekers can conveniently search for homes at the click of a button. It offers a wide selection of homes for both buyers and renters in numerous locations all over Kenya. It also allows landlords and home-sellers to post their properties so that potential buyers or renters can view them and contact them.',
            'davidokwacha@gmail.com',
            [email,],
            fail_silently=False,
        )
        return super().validate(attrs)
    
    #change save to create
    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user

    def __str__(self):
        return Account


class LoginSerializer(serializers.Serializer):
    email       = serializers.CharField(required=True)
    password    = serializers.CharField(required=True, write_only=True)
    token       = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = Account
        fields = ['email', 'password', 'token',]
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def validate(self, data):
        return data

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
    class Meta:
        fields = ['email']
        
    def validate(self, attrs):
        Email = attrs.get['email','']
        
        return super.validate(attrs)
    
    
class SetPasswordSerializer(serializers.Serializer):
    
    password        = serializers.CharField( min_length = 8, write_only = True)
    token           = serializers.CharField( min_length = 1, write_only = True)
    user_id_encode  = serializers.CharField( min_length = 1, write_only = True)
    
    class Meta():
        fields      = [ 'password', 'token', 'user_id_encode', ]
        
    def validate(self, attrs):
        
        try:
            
            password        = attrs.get('password')
            token           = attrs.get('token')
            user_id_encode  = attrs.get('user_id_encode')
            
            user_id         = force_str( urlsafe_base64_decode( user_id_encode))
            user            = Account.objects.get( id = user_id )
            
            if not PasswordResetTokenGenerator().check_token( user,token ):
                raise AuthenticationFailed ( ' Reset link is invalid', 401 )
            
            user.set_password(password)
            user.save()
            
            
        except Exception as e:
            raise AuthenticationFailed ( ' Reset link is invalid', 401 )
        
        
        return super().validate(attrs)