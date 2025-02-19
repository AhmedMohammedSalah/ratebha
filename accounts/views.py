
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import ListView

from .models import Services
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import ServiceForm
# Create your views here.
# 
class CreateServiceView(CreateView):
    model = Services
    fields = ['service_image']
    template_name = 'add-work.html' 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('accounts:profile')

    def post(self, request):
        form = ServiceForm(request.POST, request.FILES)  # استبدل YourForm بالنموذج المناسب
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('accounts:profile'))
        return super().post(request)

class ServiceListView(LoginRequiredMixin, ListView):
    model = Services
    template_name = 'profile.html'  # اسم قالب عرض القائمة الخاص بك
    context_object_name = 'services'

    def get_queryset(self):
        return Services.objects.filter(user=self.request.user)
# 
class LoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # تعديل وتخصيص حقول النموذج هنا إن لزم الأمر
        form.fields['username'].widget.attrs['class'] = 'input'
        form.fields['password'].widget.attrs['class'] = 'input'
        form.fields['username'].label =""
        form.fields['password'].label =""
        form.fields['username'].widget.attrs['placeholder'] = "username"
        form.fields['password'].widget.attrs['placeholder'] = "password"

        return form
    
from .forms import CustomUserCreationForm
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # تعديل وتخصيص حقول النموذج هنا إن لزم الأمر
        form.fields['username'].label =""
        form.fields['username'].help_text =""
        form.fields['username'].widget.attrs['class'] = 'input'
        form.fields['username'].widget.attrs['placeholder'] = "username"
        form.fields['phone'].label =""
        form.fields['phone'].widget.attrs['class'] = 'input'
        form.fields['phone'].widget.attrs['placeholder'] = "Phone"
        form.fields['email'].label =""
        form.fields['email'].widget.attrs['class'] = 'input'
        form.fields['email'].widget.attrs['placeholder'] = "Email"
        form.fields['address'].label =""
        form.fields['address'].widget.attrs['class'] = 'input'
        form.fields['address'].widget.attrs['placeholder'] = "adress"
        
        form.fields['password1'].widget.attrs['class'] = 'input'
        form.fields['password1'].label =""
        form.fields['password1'].widget.attrs['placeholder'] = "password"
        form.fields['password2'].widget.attrs['class'] = 'input'
        form.fields['password2'].label =""
        form.fields['password2'].help_text =""
        form.fields['password1'].help_text =""
        form.fields['password2'].widget.attrs['placeholder'] = "Confirm password"

        return form
    def form_valid(self, form):
        form.instance.is_customer = True
        return super().form_valid(form)
    
class SignUpServiceProviderView(CreateView):
    template_name = 'registration/signup_service_provider.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # تعديل وتخصيص حقول النموذج هنا إن لزم الأمر
        form.fields['username'].label =""
        form.fields['username'].help_text =""
        form.fields['username'].widget.attrs['class'] = 'input'        
        form.fields['service'].label =""
        form.fields['service'].help_text =""
        form.fields['service'].widget.attrs['class'] = 'input'
        form.fields['username'].widget.attrs['placeholder'] = "username"
        form.fields['phone'].label =""
        form.fields['phone'].widget.attrs['class'] = 'input'
        form.fields['phone'].widget.attrs['placeholder'] = "Phone"
        form.fields['email'].label =""
        form.fields['email'].widget.attrs['class'] = 'input'
        form.fields['email'].widget.attrs['placeholder'] = "Email"
        form.fields['address'].label =""
        form.fields['address'].widget.attrs['class'] = 'input'
        form.fields['address'].widget.attrs['placeholder'] = "adress"
        form.fields['image'].label =""
        form.fields['image'].widget.attrs['class'] = 'input'
        form.fields['image'].widget.attrs['placeholder'] = "Upload Image"
        
        form.fields['password1'].widget.attrs['class'] = 'input'
        form.fields['password1'].label =""
        form.fields['password1'].widget.attrs['placeholder'] = "password"
        form.fields['password2'].widget.attrs['class'] = 'input'
        form.fields['password2'].label =""
        form.fields['password2'].help_text =""
        form.fields['password1'].help_text =""
        form.fields['password2'].widget.attrs['placeholder'] = "Confirm password"

        return form
    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    def form_valid(self, form):
        form.instance.is_service_provider = True
        return super().form_valid(form)
