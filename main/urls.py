from django.urls import path
from django.views.generic import TemplateView

from .views import ContactUsView

from main import views

urlpatterns = [
    path('about-us/', TemplateView.as_view(template_name='about_us.html')),
    path('',TemplateView.as_view(template_name='home.html')),
    path('contact-us/',ContactUsView.as_view(),name='contact-us'),
]