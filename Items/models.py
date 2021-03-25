from django.db import models
from  Authentication.models import  Account
from django.db.models import CharField

# Create your models here.

class Key_features(models.Model):
    product_feature     = models.TextField()
    
    def __str__(self):
        return self.product_feature
    
    
class  Product_specifications(models.Model):
    product_specification   = models.TextField()
    
    def __str__(self):
        return self.product_specification

class  Product_details(models.Model):
    product_image       = models.ImageField( blank=False)
    product_name        = models.CharField( blank=False)
    category            = models.CharField( blank=False)
    sub_category        = models.CharField( blank=False)
    admin_id            = models.ForeignKey( Account, on_delete=models.SET_NULL, blank= True , null=True , related_name="product_upload_admin")
    date_uploaded       = models.DateTimeField( auto_now_add = True, null =True)
    
    old_price           = models.IntegerField()
    new_price           = models.IntegerField()
    product_description = models.CharField()
    key_features        = models.ManyToManyField(key_features, blank=True)
    product_specifications = models.ManyToManyField(product_description, blank=True)
    
    def __str__(self):
        return self.product_name + ' ' + self.category
    
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


class  Order(models.Model):
    pass
