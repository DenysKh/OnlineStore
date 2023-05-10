from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<slug:product_id>', cart_add, name='cart_add'),
    path('remove/<slug:product_id>', cart_remove, name='cart_remove'),
]