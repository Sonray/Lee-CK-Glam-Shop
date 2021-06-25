from django.db import models
from  Authentication.models import  Account
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.conf import settings
from tinymce.models import HTMLField

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
    product_description = HTMLField(blank=True, null=True)
    key_features        = HTMLField(blank=True, null=True)
    in_the_box          = HTMLField(blank=True, null=True)
    specifications      = HTMLField(blank=True, null=True)
    
    def __str__(self):
        return self.product_name
    
    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()
    

class Product_images(models.Model):
    
    class  Meta:
        verbose_name_plural = 'Product_images'
    
    product             = models.ForeignKey( Product_details,on_delete = models.CASCADE , related_name="Product_image_id" , null=True, blank= True)
    image               = models.ImageField(upload_to='products/', blank=False, null=True)
    
    def save_review(self):
        self.save()

    def delete_review(self):
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
        
