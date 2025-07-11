from django.urls import path

from app.views import *

urlpatterns = [
    path('contact', ContactCreateAPIView.as_view(), name='contact-create'),
    path('faq/<str:language_prefix>', FaqListAPIView.as_view(), name='contact-create'),
    path("about/<str:language_prefix>", AboutListAPIView.as_view(), name="about-list"),
    path("category", CategoryListAPIView.as_view(), name="category-list"),
    path("products/<str:language_prefix>", ProductList.as_view(), name="products-list"),
    path("product/<str:language_prefix>/<int:pk>", ProductListAPIView.as_view(), name="product-detail"),

]
