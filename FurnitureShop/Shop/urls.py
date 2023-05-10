from django.conf.urls.static import static
from django.urls import path

from FurnitureShop import settings
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('category/<slug>', product_list, name='product_list_by_category'),
    path('product_detail/<id>/<slug>', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
