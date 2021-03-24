from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import RegisterUser, LoginUser, PasswordTokenCheck, ResetPassword, SetPassword
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [

    url(r'register/', RegisterUser.as_view(), name='register'),
    url(r'login/', LoginUser.as_view(), name='Login'),
    url(r'reset-email/', ResetPassword.as_view(), name='reset-email'),
    path('reset-password/<user_id_encode>/<token>/', PasswordTokenCheck.as_view(), name='reset-password'),
    path('set-password', SetPassword.as_view(), name='set-password'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)