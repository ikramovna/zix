from django.urls import path

from app.views import *

urlpatterns = [
    path('contact', ContactCreateAPIView.as_view(), name='contact-create'),
    path("category/<str:language_prefix>", CategoryListAPIView.as_view(), name="category-list"),
    path("product/<str:language_prefix>", ProductListAPIView.as_view(), name="product-list"),
]
