from django.db import models
from  Items.models import  Product_details
from django.conf import settings

# Create your models here.


delivery_status = (
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
    ('failed', 'Failed')
)

class Order(models.Model):
        
    user_id             = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="User_order")
    date_ordered        = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    order_id            = models.CharField(max_length=50, blank=False, null=False, unique=True, default='ABC123')
    payment_id          = models.CharField(max_length=150,blank=True, null=True)
    amount_paid         = models.IntegerField(blank=True, null=True)
    Payment_method      = models.CharField(max_length=50, blank=True, null=True)
    delivery_method     = models.CharField(max_length=50, blank=True, null=True)
    payment_status      = models.BooleanField(default=False, blank=True, null=True)
    order_status        = models.CharField(max_length=50, blank=True, null=True, choices=delivery_status)
    
    
    def __str__(self):
        return self.order_id
        
    @property
    def orderitems(self):
        return self.order_items_set.all()
    
    @property
    def customerpick(self):
        return self.customer_pickup_point_set.all()
    
    class  Meta:
        verbose_name_plural = 'Orders'
        ordering = ['-date_ordered']

      
class Ordered_Items(models.Model):
        
    order_id            = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Ordered_Items_Order_id" , null=True, blank= False)
    date                = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    product             = models.ForeignKey( Product_details,on_delete = models.CASCADE , related_name="Ordered_Items_product" , null=True, blank= True)
    quantity            = models.IntegerField(blank=True, null=True)
    price               = models.IntegerField(blank=True, null=True)
           
    class  Meta:
        verbose_name_plural = 'Ordered_Items'
        ordering = ['-date']


class Pickup_stations(models.Model):
    '''
        Pickup agent in various counties and cities in the region
    '''
        
    user_id             = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="Pickup_stations_user_id")
    date                = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    phone_number        = models.CharField(max_length=50,blank=True, null=True)
    Address_Landmark    = models.CharField(max_length=150,blank=True, null=True)
    Address_information = models.CharField(max_length=150,blank=True, null=True)
    service_hours       = models.CharField(max_length=150,blank=True, null=True)
    County              = models.CharField(max_length=50,blank=True, null=True)
    City                = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return self.County
    
    class  Meta:
        verbose_name_plural = 'Pickup_stations'
        ordering = ['-date']
       

class Customer_Pickup_point(models.Model):
        
    order_id            = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="customer_pickup_order_id" , null=True, blank= False)
    date                = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user_id             = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="Customer_Pickup_point_user_id")
    Station_id          = models.ForeignKey( Pickup_stations,on_delete = models.CASCADE , related_name="Pickup_stations" , null=True, blank= False)
    first_name          = models.CharField(max_length=30,blank=True, null=True)
    last_name           = models.CharField(max_length=30,blank=True, null=True)
    phone_number        = models.CharField(max_length=50,blank=True, null=True)
    Delivery_address    = models.CharField(max_length=150,blank=True, null=True)
    County              = models.CharField(max_length=50,blank=True, null=True)
    City                = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return self.County
    
    
    class  Meta:
        verbose_name_plural = 'Customer_Pickup_points'
        ordering = ['-date']
        

class Pending_Order(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Pending_Orders'
    
    order_id                    = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Pending_Order" , null=True, blank= False)
    date                        = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    order_received_by_customer  = models.BooleanField(default=False,blank=True, null=True)
    
    def __str__(self):
        return self.Pending_Orders    


class Order_Received_by_Customer(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Orders_Received'
    
    order_id            = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Orders_Received" , null=True, blank= False)
    date                = models.DateTimeField(auto_now_add=True, blank=True, null=True)
        
    def __str__(self):
        return self.Order_Received_by_Customer  


class Mpesa_Order_payments(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Mpesa_Order_payments'
    
    payment_id              = models.CharField(max_length=50, blank=True, null=True)
    date_paid               = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user_id                 = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="Mpesa_Order_payments_user_id")
    order_id                = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Mpesa_Order_payments_Order_id" , null=True, blank= False)
    amount_paid             = models.IntegerField(blank=True, null=True)
    payment_status          = models.BooleanField(default=False, blank=True, null=True)
    phone_number            = models.CharField(max_length=50, blank=True, null=True)
            
    def __str__(self):
        return self.Mpesa_Order_payments


class Paypal_Order_payments(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Paypal_Order_payments'
    
    payment_id              = models.CharField(max_length=50, blank=True, null=True)
    date_paid               = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user_id                 = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="Paypal_Order_payments_user_id")
    order_id                = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Paypal_Order_payments_Order_id" , null=True, blank= False)
    amount_paid             = models.IntegerField(blank=True, null=True)
    payment_status          = models.BooleanField(default=False, blank=True, null=True)
    email                   = models.CharField(max_length=150, blank=True, null=True)
            
    def __str__(self):
        return self.Paypal_Order_payments
