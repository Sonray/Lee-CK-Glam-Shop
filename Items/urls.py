from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import Display_all_products, Display_specific_product,Display_all_Reviews, Make_a_review

urlpatterns = [

    path('display-products', Display_all_products.as_view(), name='display-products' ),
    path('product/<int:pk>', Display_specific_product.as_view(), name='products' ),
    path('review', Make_a_review.as_view(), name='review' ),
    path('display-reviews', Display_all_Reviews.as_view(), name='display-review' ),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)