from django.contrib import admin
from  .models import Order, Paypal_Order_payments,Mpesa_Order_payments,Customer_Pickup_point,Pickup_stations, Ordered_Items, Order_Received_by_Customer,Pending_Order

#change Admin page appearance

class OrderAdmin(admin.ModelAdmin):
    list_display        = ('user_id','date_ordered','order_id', 'payment_id', 'amount_paid', 'Payment_method', 'delivery_method', 'payment_status', 'order_status')
    search_fields       =  ('user_id__email', 'date_ordered','order_id', 'payment_id', 'amount_paid', 'Payment_method', 'delivery_method', 'payment_status', 'order_status')
    ordering            = ('-date_ordered',)
    list_filter         = ('date_ordered', 'delivery_method', 'delivery_method', 'payment_status', 'order_status', )
    raw_id_fields       = ('user_id',)

class Ordered_ItemsAdmin(admin.ModelAdmin):
    list_display        = ('order_id','date', 'product', 'quantity', 'price')
    search_fields       = ('order_id__order_id','date', 'product__product_name', 'quantity', 'price')
    ordering            = ('-date',)
    list_filter         = ('date', 'order_id', )
    raw_id_fields       = ('order_id', 'product',)


class Pickup_stationsAdmin(admin.ModelAdmin):
    list_display        = ('user_id','date', 'phone_number', 'Address_Landmark', 'Address_information', 'service_hours', 'County', 'City')
    search_fields       = ('user_id__email','date', 'phone_number', 'Address_Landmark', 'Address_information', 'service_hours', 'County', 'City')
    ordering            = ('Address_information',)
    list_filter         = ('date', 'County', 'City', )
    raw_id_fields       = ('user_id', )
    

class Customer_PickupAdmin(admin.ModelAdmin):
    list_display        = ('id','user_id','date', 'order_id', 'Station_id', 'first_name', 'last_name','phone_number', 'Delivery_address', 'County', 'City')
    search_fields       = ('id','user_id__email','date', 'order_id__order_id', 'Station_id__County', 'first_name', 'last_name','phone_number', 'Delivery_address', 'County', 'City')
    ordering            = ('-date',)
    list_filter         = ('date', 'order_id', 'County', 'City', 'Station_id',)
    raw_id_fields       = ('user_id', 'order_id', 'Station_id', )
    

class Mpesa_OrderAdmin(admin.ModelAdmin):
    list_display        = ('id','user_id','date_paid', 'payment_id', 'order_id', 'amount_paid', 'payment_status', 'phone_number')
    search_fields       = ('id','user_id__email','date_paid', 'payment_id', 'order_id__order_id', 'amount_paid', 'payment_status', 'phone_number' )
    ordering            = ('-date_paid',)
    list_filter         = ('date_paid', 'payment_status', )
    raw_id_fields       = ('order_id', )
    

class Paypal_OrderAdmin(admin.ModelAdmin):
    list_display        = ('id','user_id','date_paid', 'payment_id', 'order_id', 'amount_paid', 'payment_status', 'email')
    search_fields       = ('id','user_id__email','date_paid', 'payment_id', 'order_id__order_id', 'amount_paid', 'email')
    ordering            = ('-date_paid',)
    list_filter         = ('date_paid', 'payment_status', )
    raw_id_fields       = ('order_id', )
    

class Order_Received_by_CustomerAdmin(admin.ModelAdmin):
    list_display        = ('id','order_id','date',)
    search_fields       = ('id','order_id__order_id','date',)
    ordering            = ('-date',)
    list_filter         = ('date', )
    raw_id_fields       = ('order_id', )
    

class Pending_OrderAdmin(admin.ModelAdmin):
    list_display        = ('id','order_id','date', 'order_received_by_customer',)
    search_fields       = ('id','order_id__order_id','date', 'order_received_by_customer',)
    ordering            = ('-date',)
    list_filter         = ('date', 'order_received_by_customer', )
    raw_id_fields       = ('order_id', )
        
    
# Register your models here.

admin.site.register( Order, OrderAdmin )
admin.site.register( Ordered_Items, Ordered_ItemsAdmin )
admin.site.register( Pickup_stations, Pickup_stationsAdmin )
admin.site.register( Customer_Pickup_point, Customer_PickupAdmin )
admin.site.register( Mpesa_Order_payments, Mpesa_OrderAdmin )
admin.site.register( Paypal_Order_payments, Paypal_OrderAdmin )
admin.site.register( Order_Received_by_Customer, Order_Received_by_CustomerAdmin )
admin.site.register( Pending_Order, Pending_OrderAdmin )