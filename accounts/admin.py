from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser ,Services


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'is_customer',
        'is_service_provider', 
        'slug',
        'address',
        'phone',
        'service',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {
        "fields":  (
        'is_customer',
        'is_service_provider', 
        'slug',
        'address',
        'phone',
        'service',  )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {
        "fields":  (
        'is_customer',
        'is_service_provider', 
        'slug',
        'address',
        'phone',
        'service',  )}),)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register( Services)
