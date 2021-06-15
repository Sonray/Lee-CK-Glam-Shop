from django.db import models
from  Authentication.models import  Account
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.conf import settings

# Create your models here.

class  Product_details(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Products'
    
    product_image       = models.ImageField(upload_to='products/', blank=False, null=True)
    product_name        = models.CharField( blank=False, max_length=120, null=True)
    category            = models.ManyToManyField('Category', blank=False )
    sub_category        = models.ManyToManyField('Sub_category', blank=False )
    admin_id            = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="product_upload_admin")
    date_uploaded       = models.DateTimeField( auto_now_add = True, null =True)
    old_price           = models.IntegerField(blank=True, null=True)
    new_price           = models.IntegerField(blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    key_features        = models.TextField(blank=True, null=True)
    in_the_box          = models.TextField(blank=True, null=True)
    specifications      = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.product_name
    
    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()
    
    
class Reviews(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Reviews'
    
    product             = models.ForeignKey( Product_details,on_delete = models.CASCADE , related_name="Product_review" , null=True, blank= True)
    user_id             = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="Product_review_user")
    date_reviewed       = models.DateTimeField( auto_now_add = True, null=True)
    Product_review      = models.TextField( blank=False, null=True)
    product_rating      = models.IntegerField( blank=False, null=True)
    
    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()


class Category(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Categories'
    
    category        = models.CharField(max_length=40, blank=True, null=True)
    
    def __str__(self):
        return self.category


class Sub_category(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Sub_categories'
    
    category            = models.ForeignKey( Category,on_delete = models.CASCADE , related_name="Category" , null=True, blank= True)
    sub_category        = models.CharField(max_length=40, blank=True, null=True)
    
    def __str__(self):
        return self.sub_category


class Order(models.Model):
        
    user_id             = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="User_order")
    date_ordered        = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    payment_id          = models.IntegerField(blank=True, null=True)
    amount_paid         = models.IntegerField(blank=True, null=True)
    Payment_method      = models.CharField(max_length=50, blank=True, null=True)
    delivery_method     = models.CharField(max_length=50, blank=True, null=True)
    payment_status      = models.BooleanField(default=False, blank=True, null=True)
    order_status        = models.TextField(max_length=150, blank=True, null=True)
        
    
    def __str__(self):
        return self.id
    
    
    class  Meta:
        verbose_name_plural = 'Orders'
        ordering = ['-date_ordered']

      
class Ordered_Items(models.Model):
        
    order_id            = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Ordered_Items_Order_id" , null=True, blank= False)
    date                = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    product             = models.ForeignKey( Product_details,on_delete = models.CASCADE , related_name="Ordered_Items_product" , null=True, blank= True)
    quantity            = models.IntegerField(blank=True, null=True)
    price               = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.id
    
    
    class  Meta:
        verbose_name_plural = 'Ordered_Items'
        ordering = ['-date']


class Pickup_stations(models.Model):
    '''
        Pickup agent in various counties and cities in the region
    '''
        
    user_id             = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="Pickup_stations_user_id")
    date                = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    phone_number        = models.IntegerField()
    Address_Landmark    = models.CharField(max_length=150,blank=True, null=True)
    Address_information = models.CharField(max_length=150,blank=True, null=True)
    service_hours       = models.CharField(max_length=150,blank=True, null=True)
    County              = models.CharField(max_length=50,blank=True, null=True)
    City                = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return self.id
    
    
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
    phone_number        = models.IntegerField(blank=True, null=True)
    Delivery_address    = models.CharField(max_length=150,blank=True, null=True)
    County              = models.CharField(max_length=50,blank=True, null=True)
    City                = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return self.id
    
    
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
            
    def __str__(self):
        return self.Paypal_Order_payments


class VISA_Order_payments(models.Model):
    
    class  Meta:
        verbose_name_plural = 'VISA_Order_payments'
    
    payment_id              = models.CharField(max_length=50, blank=True, null=True)
    date_paid               = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user_id                 = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="VISA_Order_payments_user_id")
    order_id                = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="VISA_Order_payments_Order_id" , null=True, blank= False)
    amount_paid             = models.IntegerField(blank=True, null=True)
    payment_status          = models.BooleanField(default=False, blank=True, null=True)
            
    def __str__(self):
        return self.VISA_Order_payments


class Mastercard_Order_payments(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Mastercard_Order_payments'
    
    payment_id              = models.CharField(max_length=50, blank=True, null=True)
    date_paid               = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user_id                 = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="Mastercard_Order_payments_user_id")
    order_id                = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Mastercard_Order_payments_Order_id" , null=True, blank= False)
    amount_paid             = models.IntegerField(blank=True, null=True)
    payment_status          = models.BooleanField(default=False, blank=True, null=True)
            
    def __str__(self):
        return self.Mastercard_Order_payments

