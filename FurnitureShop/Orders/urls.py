from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('create/pickup/', order_create_pickup, name='order_create_pickup'),
]
