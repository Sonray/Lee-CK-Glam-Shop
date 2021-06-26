from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Order_Product_Paypal, Order_Product_MPESA, Update_Customer_Pickup, Delete_Customer_Address, Display_Order_Items, Display_Customer_Pickup, Display_all_pickupstations, Display_Customer_Order

urlpatterns = [

    path('Mpesa-payment/', Order_Product_MPESA.as_view(), name='make_order_mpesa' ),
    path('paypal-payment/', Order_Product_Paypal.as_view(), name='make_order_paypal' ),
    path('customer-address/<int:pk>', Display_Customer_Pickup.as_view(), name='customer_address' ),
    path('pickup-stations/', Display_all_pickupstations.as_view(), name='Display_pickupstations' ),
    path('customer-order/<int:pk>', Display_Customer_Order.as_view(), name='Display_CustomerOrder' ),
    path('ordered-items/<int:pk>', Display_Order_Items.as_view(), name='Display_OrderItems' ),
    path('delete-customeraddress/<int:pk>', Delete_Customer_Address.as_view(), name='Delete_CustomerAddress' ),
    path('update-customeraddress/<int:pk>', Update_Customer_Pickup.as_view(), name='Update_CustomerAddress' ),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)