"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name='base.html'), name='home'),

    path("wedding", TemplateView.as_view(
        template_name='events/wedding.html'), name='wedding'),
    path("party", TemplateView.as_view(
        template_name='events/party.html'), name='party'),
    path("engagement", TemplateView.as_view(
        template_name='events/engagement.html'), name='engagement'),
    path("event", TemplateView.as_view(
        template_name='events/event.html'), name='event'),
    path("graduation", TemplateView.as_view(
        template_name='events/graduation.html'), name='graduation'),
    path("birthday", TemplateView.as_view(
        template_name='events/birthday.html'), name='birthday'),

    path("agency", TemplateView.as_view(
        template_name='services/agency.html'), name='agence'),
    path("celebrate", TemplateView.as_view(
        template_name='services/celebrate.html'), name='celebrate'),
    path("decoration", TemplateView.as_view(
        template_name='services/decoration.html'), name='decoration'),
    path("dj", TemplateView.as_view(
        template_name='services/dj.html'), name='dj'),
    path("hall", TemplateView.as_view(
        template_name='services/hall.html'), name='hall'),
    path("hotel", TemplateView.as_view(
        template_name='services/hotel.html'), name='hotel'),
    path("makup", TemplateView.as_view(
        template_name='services/makup.html'), name='makup'),
    path("photographer", TemplateView.as_view(
        template_name='services/photographer.html'), name='photographer'),
    path("agency", TemplateView.as_view(
        template_name='services/agency.html'), name='agency'),
    path("SuitsDress", TemplateView.as_view(
        template_name='services/SuitsDress.html'), name='SuitsDress'),
    path("uniform", TemplateView.as_view(
        template_name='services/uniform.html'), name='uniform'),
    path("workspace", TemplateView.as_view(
        template_name='services/workspace.html'), name='workspace'),
    
    path("mm", TemplateView.as_view(
        template_name='pr/profile.html'), name='mm'),
    
    path("nn", TemplateView.as_view(
        template_name='pr/profile1.html'), name='nn'),
    path("ss", TemplateView.as_view(
        template_name='pr/reservation.html'), name='ss'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
