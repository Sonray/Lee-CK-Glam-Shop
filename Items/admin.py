from django.contrib import admin
from  .models import Product_details, Order, Reviews,Category,Sub_category, Order_Made_by_Mpesa, Order_Received_by_Customer,Pending_Order

# Register your models here.

admin.site.register( Product_details )
admin.site.register( Order )
admin.site.register( Reviews )
admin.site.register( Category )
admin.site.register( Sub_category )
admin.site.register( Order_Made_by_Mpesa )
admin.site.register( Order_Received_by_Customer )
admin.site.register( Pending_Order )