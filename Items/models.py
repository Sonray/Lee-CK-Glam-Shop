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
    
    class  Meta:
        verbose_name_plural = 'Orders'
    
    user_id             = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank= True , null=True , related_name="User_order")
    product             = models.ForeignKey( Product_details,on_delete = models.CASCADE , related_name="Product_order" , null=True, blank= True)
    first_name          = models.CharField(max_length=40)
    last_name           = models.CharField(max_length=40)
    phone_number        = models.IntegerField(max_length=20)
    phone_number_2      = models.IntegerField(max_length=40)
    delivery_address    = models.CharField(max_length=40)
    region              = models.CharField(max_length=40)
    city                = models.CharField(max_length=40)
    delivery_method     = models.CharField(max_length=40)
    price               = models.IntegerField(max_length=40)
    date_of_order       = models.DateTimeField(auto_now_add=True)
    billing_status      = models.BooleanField(default=False)
    order_received      = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return self.sub_category
    
    
