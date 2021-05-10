from django.db import models
from  Authentication.models import  Account
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.conf import settings

# Create your models here.

class  Product_details(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Products'
    
    product_image       = models.ImageField(upload_to='products/', blank=False)
    product_name        = models.CharField( blank=False, max_length=120)
    category            = models.ManyToManyField('Category', blank=False )
    sub_category        = models.ManyToManyField('Sub_category', blank=False )
    admin_id            = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="product_upload_admin")
    date_uploaded       = models.DateTimeField( auto_now_add = True, null =True)
    
    old_price           = models.IntegerField()
    new_price           = models.IntegerField()
    product_description = models.TextField()
    key_features        = models.TextField()
    in_the_box          = models.TextField()
    specifications      = models.TextField()
    
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
    date_reviewed       = models.DateTimeField( auto_now_add = True, null =True)
    Product_review      = models.TextField( blank=False)
    product_rating      = models.IntegerField( blank=False)
    
    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()


class Category(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Categories'
    
    category        = models.CharField(max_length=40)
    
    def __str__(self):
        return self.category


class Sub_category(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Sub_categories'
    
    sub_category        = models.CharField(max_length=40)
    
    def __str__(self):
        return self.sub_category


class Order(models.Model):
        
    user_id             = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="User_order")
    product             = models.ForeignKey( Product_details,on_delete = models.CASCADE , related_name="Product_order" , null=True, blank= True)
    first_name          = models.CharField(max_length=40, blank=True, null=True)
    last_name           = models.CharField(max_length=40, blank=True, null=True)
    phone_number        = models.BigIntegerField( blank=True, null=True)
    order_phone_number  = models.BigIntegerField( blank=True, null=True)
    delivery_address    = models.CharField(max_length=40, blank=True, null=True)
    region              = models.CharField(max_length=40, blank=True, null=True)
    city                = models.CharField(max_length=40, blank=True, null=True)
    delivery_method     = models.CharField(max_length=40, blank=True, null=True)
    price               = models.IntegerField( blank=True, null=True)
    date_of_order       = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    CheckoutRequestID   = models.CharField(max_length=50, blank=True, null=True)
    MerchantRequestID   = models.CharField(max_length=50, blank=True, null=True)
    billing_status      = models.BooleanField(default=False, blank=True, null=True)
    order_pending       = models.BooleanField(default=False, blank=True, null=True)
    Order_items         = models.ManyToManyField('Product_details', blank=False, related_name="Order_items" )
        
        
    def __str__(self):
        return self.delivery_method
    
    
    class  Meta:
        verbose_name_plural = 'Orders'
        ordering = ['-date_of_order']
    


class Pending_Order(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Pending_Orders'
    
    order_id                    = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Pending_Order" , null=True, blank= False)
    order_dispatched            = models.BooleanField(default=False)
    order_received_by_customer  = models.BooleanField(default=False)
    
    def __str__(self):
        return self.Pending_Orders    


class Order_Received_by_Customer(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Orders_Received'
    
    order_id            = models.ForeignKey( Order,on_delete = models.CASCADE , related_name="Orders_Received" , null=True, blank= False)
    
        
    def __str__(self):
        return self.Order_Received_by_Customer  


class Order_Made_by_Mpesa(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Orders_Made_by_Mpesa'
    
    CheckoutRequestID       = models.CharField(max_length=50, blank=True, null=True)
    MerchantRequestID       = models.CharField(max_length=50, blank=True, null=True)
    ResultCode              = models.IntegerField(blank=True, null=True)
    ResultDesc              = models.CharField(max_length=120, blank=True, null=True)
    Amount                  = models.FloatField(default=0)
    MpesaReceiptNumber      = models.CharField(max_length=120, blank=True, null=True)
    TransactionDate         = models.DateField( blank=True, null=True)
    PhoneNumber             = models.CharField(max_length=120, blank=True, null=True)
        
    def __str__(self):
        return self.Order_Made_by_Mpesa
