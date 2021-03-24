from django.db import models
from  Authentication.models import  Account
from django.db.models import CharField

# Create your models here.

class  Product_details(models.Model):
    product_image       = models.ImageField( blank=False)
    product_name        = models.CharField( blank=False)
    category            = models.CharField( blank=False)
    sub_category        = models.CharField( blank=False)
    admin_id            = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="product_upload")
    date_uploaded       = models.DateTimeField(auto_now_add = True, null =True)
    
    old_price           = models.IntegerField()
    new_price           = models.IntegerField()
    product_description = models.CharField()
    

    
