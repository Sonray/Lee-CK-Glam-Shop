from django.db import models
from  Authentication.models import  Account
from cloudinary.models import CloudinaryField

# Create your models here.

class Key_features(models.Model):
    product_feature     = models.TextField()    
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.product_feature
    
    
class  Product_specifications(models.Model):
    product_specification   = models.TextField()
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.product_specification


class Whats_packaged(models.Model):
    in_the_box          = models.TextField()
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
        
    def __str__(self):
        return self.in_the_box


class Category(models.Model):
    category        = models.CharField(max_length=40)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.category


class Sub_category(models.Model):
    sub_category        = models.CharField(max_length=40)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.sub_category



class  Product_details(models.Model):
    product_image       = CloudinaryField('LeeGlam/', blank=False)
    product_name        = models.CharField( blank=False, max_length=120)
    category            = models.ManyToManyField( Category )
    sub_category        = models.ManyToManyField( Sub_category )
    admin_id            = models.ForeignKey( Account, on_delete=models.SET_NULL, blank= True , null=True , related_name="product_upload_admin")
    date_uploaded       = models.DateTimeField( auto_now_add = True, null =True)
    
    old_price           = models.IntegerField()
    new_price           = models.IntegerField()
    product_description = models.TextField()
    key_features        = models.ManyToManyField(Key_features)
    in_the_box          = models.ManyToManyField(Whats_packaged)
    specifications      = models.ManyToManyField(Product_specifications)
    
    def __str__(self):
        return self.product_name
    
    def save_product(self):
        self.save()

    def delete_product(self):
        self.delete()
    
    
class Reviews(models.Model):
    product             = models.ForeignKey( Product_details,on_delete = models.CASCADE , related_name="Product_review")
    user_id             = models.ForeignKey( Account, on_delete=models.SET_NULL, blank= True , null=True , related_name="Product_review_user")
    date_reviewed       = models.DateTimeField( auto_now_add = True, null =True)
    Product_review      = models.TextField( blank=False)
    product_rating      = models.IntegerField( blank=False)
    
    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()


