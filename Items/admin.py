from django.contrib import admin
from  .models import  Key_features, Product_details, Product_specifications, 
        Whats_packaged,Reviews,Category,Sub_category

# Register your models here.

admin.site.register( Key_features )
admin.site.register( Product_details )
admin.site.register( Product_specifications )
admin.site.register( Whats_packaged )
admin.site.register( Reviews )
admin.site.register( Category )
admin.site.register( Sub_category )