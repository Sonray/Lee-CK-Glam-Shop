from django.contrib import admin
from  .models import Product_details, Order, Reviews,Category,Sub_category

# Register your models here.

admin.site.register( Product_details )
admin.site.register( Order )
admin.site.register( Reviews )
admin.site.register( Category )
admin.site.register( Sub_category )