from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import RegisterUser
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    url(r'/register/', RegisterUser.as_view(), name='register'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)