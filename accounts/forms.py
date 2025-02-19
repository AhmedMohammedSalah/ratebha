from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Services

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['service_image','user']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'email',
            'is_customer',
            'is_service_provider',
            'slug',
            'address',
            'phone',
            'service',
            'image',
            )


class AdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'is_customer',
            'is_service_provider',
            'slug',
            'address',
            'phone',
            'service',
            'image',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

# class EmailAuthenticationForm(AuthenticationForm):
#     username = forms.EmailField(label='Email')
