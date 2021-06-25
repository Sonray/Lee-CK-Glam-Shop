from django.contrib import admin
from  .models import Product_details, Reviews,Category,Sub_category,Product_images
#change Admin page appearance


class ProductAdmin(admin.ModelAdmin):
    list_display        = ('id','product_name','date_uploaded', 'old_price', 'new_price', 'product_description', 'key_features', 'in_the_box', 'specifications')
    search_fields       =  ('product_name', 'new_price', 'product_description', 'key_features','in_the_box', 'specifications','date_uploaded')
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('product_name',)
    

class OrderAdmin(admin.ModelAdmin):
    list_display        = ('id','user_id','date_ordered', 'payment_id', 'amount_paid', 'Payment_method', 'delivery_method', 'payment_status', 'order_status')
    search_fields       =  ('user_id', 'date_ordered', 'payment_id', 'amount_paid', 'Payment_method', 'delivery_method', 'payment_status', 'order_status')
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('date_ordered',)


class ReviewAdmin(admin.ModelAdmin):
    list_display        = ('id','user_id','date_reviewed', 'product', 'Product_review', 'product_rating')
    search_fields       =  ('id','user_id','date_reviewed', 'product', 'Product_review', 'product_rating')
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('date_reviewed',)
    

class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('id','category')
    search_fields       =  ('id','category')
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('category',)
    

class SubCategoryAdmin(admin.ModelAdmin):
    list_display        = ('id','category','sub_category',)
    search_fields       =  ('id','category','sub_category',)
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('sub_category',)
    
    
class Product_imagesAdmin(admin.ModelAdmin):
    list_display        = ('id','product','image', )
    search_fields       = ('id','product','image', )
    # readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('product',)
    
    
# Register your models here.

admin.site.register( Product_details, ProductAdmin )
admin.site.register( Reviews, ReviewAdmin )
admin.site.register( Category, CategoryAdmin )
admin.site.register( Sub_category, SubCategoryAdmin )
admin.site.register( Product_images, Product_imagesAdmin )