from django.urls import path
from django.views.generic.base import TemplateView  
from .views import LoginView,SignUpView,SignUpServiceProviderView,ServiceListView,CreateServiceView
app_name='accounts'
urlpatterns = [
    # account main 
    # path("signup/", CustomUserSignUpView.as_view(), name="signup"),
    path("login/",LoginView.as_view(),name="login"),
    path("signup/choose",TemplateView.as_view(template_name='customer-kind.html') ,name='signup_choose'),  
    path("signup/customer",SignUpView.as_view(),name="signup_customer"),
    path("signup/service-provider",SignUpServiceProviderView.as_view(),name="signup_service_provider"),
    path("profile",ServiceListView.as_view(),name="profile"),
    path("profile/add-work",CreateServiceView.as_view(),name="add_work"),
    
    # path('',home,name='login_home' ),
    
]