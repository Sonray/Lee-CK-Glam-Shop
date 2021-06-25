from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Order_Product_Paypal, Order_Product_MPESA

urlpatterns = [

    path('Mpesa-payment/', Order_Product_MPESA.as_view(), name='make_order_mpesa' ),
    path('paypal-payment/', Order_Product_Paypal.as_view(), name='make_order_paypal' ),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)