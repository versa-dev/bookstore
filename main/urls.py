from django.urls import path
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .views import ContactUsView
from django.contrib.auth import views as auth_views
from main import views,models,forms

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
    path('signup/',views.SignupView.as_view(),name='signup'),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            form_class=forms.AuthenticationForm,
        ),
        name="login",
    ),
    path(
        "address/",
        views.AddressListView.as_view(),
        name="address_list",
    ),
    path(
        "address/create/",
        views.AddressCreateView.as_view(),
        name="address_create",
    ),
    path(
        "address/<int:pk>/",
        views.AddressUpdateView.as_view(),
        name="address_update",
    ),
    path(
        "address/<int:pk>/delete/",
        views.AddressDeleteView.as_view(),
        name="address_delete",
    ),
]