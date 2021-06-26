from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display        = ('email', 'first_name', 'last_name', 'phone_number', 'date_joined', 'last_login', 'is_staff', 'is_admin')
    search_fields       =  ('email', 'first_name', 'last_name', 'phone_number',)
    readonly_fields     = ('date_joined', 'last_login',)
    ordering            = ('email',)

    filter_horizontal   = ()
    list_filter         = ('date_joined', 'is_admin', 'is_staff',)
    fieldsets           = ()

admin.site.register(Account, AccountAdmin)
