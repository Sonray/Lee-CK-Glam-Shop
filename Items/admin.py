from django.contrib import admin
from  .models import Product_details, Order, Reviews,Category,Sub_category,Mastercard_Order_payments,VISA_Order_payments,Paypal_Order_payments,Mpesa_Order_payments,Customer_Pickup_point,Pickup_stations, Ordered_Items, Order_Received_by_Customer,Pending_Order

# Register your models here.

admin.site.register( Product_details )
admin.site.register( Order )
admin.site.register( Reviews )
admin.site.register( Category )
admin.site.register( Sub_category )
admin.site.register( Ordered_Items )
admin.site.register( Pickup_stations )
admin.site.register( Customer_Pickup_point )
admin.site.register( Mpesa_Order_payments )
admin.site.register( Paypal_Order_payments )
admin.site.register( VISA_Order_payments )
admin.site.register( Mastercard_Order_payments )
admin.site.register( Order_Received_by_Customer )
admin.site.register( Pending_Order )