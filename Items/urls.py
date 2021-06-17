from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import Display_all_products, Display_specific_product, Order_Product_Paypal, Display_all_Reviews, Make_a_review, Search_products_category, Search_products_subcategory, Search_products,Order_Product_MPESA

urlpatterns = [

    path('display-products', Display_all_products.as_view(), name='display-products' ),
    path('product/<int:pk>', Display_specific_product.as_view(), name='products' ),
    path('review', Make_a_review.as_view(), name='review' ),
    path('display-reviews/<int:pk>', Display_all_Reviews.as_view(), name='display-review' ),
    path('search/category/', Search_products_category.as_view(), name='search-category' ),
    path('search/subcategory/', Search_products_subcategory.as_view(), name='search-subcategory' ),
    path('search/', Search_products.as_view(), name='search' ),
    path('Mpesa-payment/', Order_Product_MPESA.as_view(), name='make_order_mpesa' ),
    path('paypal-payment/', Order_Product_Paypal.as_view(), name='make_order_paypal' ),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)