from django.contrib import admin
from  .models import Product_details, Reviews,Category,Sub_category,Product_images
#change Admin page appearance


class ProductAdmin(admin.ModelAdmin):
    list_display        = ('product_name','date_uploaded', 'old_price', 'new_price', 'product_description', 'key_features', 'in_the_box', 'specifications')
    search_fields       =  ('product_name', 'new_price', 'product_description', 'key_features','in_the_box', 'specifications','date_uploaded')
    list_filter         = ('date_uploaded', 'new_price', )
    ordering            = ('product_name',)
    

class ReviewAdmin(admin.ModelAdmin):
    list_display        = ('user_id','date_reviewed', 'product', 'Product_review', 'product_rating')
    search_fields       =  ('user_id','date_reviewed', 'product', 'Product_review', 'product_rating')
    ordering            = ('date_reviewed',)
    list_filter         = ('date_reviewed', )
    

class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('category',)
    search_fields       =  ('category',)
    ordering            = ('category',)
    

class SubCategoryAdmin(admin.ModelAdmin):
    list_display        = ('category','sub_category',)
    search_fields       =  ('category','sub_category',)
    ordering            = ('sub_category',)
    
    
class Product_imagesAdmin(admin.ModelAdmin):
    list_display        = ('product','image', )
    search_fields       = ('product','image', )
    ordering            = ('product',)
    
    
# Register your models here.

admin.site.register( Product_details, ProductAdmin )
admin.site.register( Reviews, ReviewAdmin )
admin.site.register( Category, CategoryAdmin )
admin.site.register( Sub_category, SubCategoryAdmin )
admin.site.register( Product_images, Product_imagesAdmin )