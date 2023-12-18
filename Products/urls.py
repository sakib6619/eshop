from django.urls import path
from .views import *
urlpatterns = [
    path('details/<slug:slug>/', product_details, name='product_details'),
    path('shop', all_product, name='all_product')
]