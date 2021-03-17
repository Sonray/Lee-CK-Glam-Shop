from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    # url(r'/register/', name='register'),
    # # url(r'/login/', name='Login'),
    # path('reset-email', name='reset-email'),
    # path('reset-password/<user_id_encode>/<token>/', name='reset-password'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)