from django.urls import path
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .views import ContactUsView

from main import views,models

urlpatterns = [
    path('about-us/', TemplateView.as_view(template_name='about_us.html')),
    path('',TemplateView.as_view(template_name='home.html')),
    path('contact-us/',ContactUsView.as_view(),name='contact-us'),
    path(
        'products/<slug:tag>/',
         views.ProductListView.as_view(),
         name='products',
    ),
    path(
        'product/<slug:slug>/',
         DetailView.as_view(template_name='main/product_detail.html', model=models.Product),
         name='product',
    ),
    
]