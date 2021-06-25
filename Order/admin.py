from django.contrib import admin
from  .models import Product_details, Order, Paypal_Order_payments,Mpesa_Order_payments,Customer_Pickup_point,Pickup_stations, Ordered_Items, Order_Received_by_Customer,Pending_Order

#change Admin page appearance

class OrderAdmin(admin.ModelAdmin):
    list_display        = ('id','user_id','date_ordered','order_id', 'payment_id', 'amount_paid', 'Payment_method', 'delivery_method', 'payment_status', 'order_status')
    search_fields       =  ('user_id', 'date_ordered','order_id', 'payment_id', 'amount_paid', 'Payment_method', 'delivery_method', 'payment_status', 'order_status')
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('-date_ordered',)


class Ordered_ItemsAdmin(admin.ModelAdmin):
    list_display        = ('id','order_id','date', 'product', 'quantity', 'price')
    search_fields       = ('id','order_id__order_id','date', 'product__product_name', 'quantity', 'price')
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('-date',)
    

class Pickup_stationsAdmin(admin.ModelAdmin):
    list_display        = ('id','user_id','date', 'phone_number', 'Address_Landmark', 'Address_information', 'service_hours', 'County', 'City')
    search_fields       = ('id','user_id','date', 'phone_number', 'Address_Landmark', 'Address_information', 'service_hours', 'County', 'City')
    # readonly_fields   = ('date_joined', 'last_login',)
    ordering            = ('Address_information',)
    

class Customer_PickupAdmin(admin.ModelAdmin):
    list_display        = ('id','user_id','date', 'order_id', 'Station_id', 'first_name', 'last_name','phone_number', 'Delivery_address', 'County', 'City')
    search_fields       = ('id','user_id','date', 'order_id', 'Station_id', 'first_name', 'last_name','phone_number', 'Delivery_address', 'County', 'City')
    # readonly_fields   = ('date_joined', 'last_login',)
    ordering            = ('date',)
    

class Mpesa_OrderAdmin(admin.ModelAdmin):
    list_display        = ('id','order_id','date_paid', 'payment_id', 'order_id', 'amount_paid', 'payment_status')
    search_fields       = ('id','order_id','date_paid', 'payment_id', 'order_id', 'amount_paid', 'payment_status')
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('date_paid',)
    

class Order_Received_by_CustomerAdmin(admin.ModelAdmin):
    list_display        = ('id','order_id','date',)
    search_fields       = ('id','order_id','date',)
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('date',)
    

class Pending_OrderAdmin(admin.ModelAdmin):
    list_display        = ('id','order_id','date', 'order_received_by_customer',)
    search_fields       = ('id','order_id','date', 'order_received_by_customer',)
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('date',)
        
    
# Register your models here.

admin.site.register( Order, OrderAdmin )
admin.site.register( Ordered_Items, Ordered_ItemsAdmin )
admin.site.register( Pickup_stations, Pickup_stationsAdmin )
admin.site.register( Customer_Pickup_point, Customer_PickupAdmin )
admin.site.register( Mpesa_Order_payments, Mpesa_OrderAdmin )
admin.site.register( Paypal_Order_payments, Mpesa_OrderAdmin )
admin.site.register( Order_Received_by_Customer, Order_Received_by_CustomerAdmin )
admin.site.register( Pending_Order, Pending_OrderAdmin )