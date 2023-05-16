from django.conf.urls.static import static
from django.urls import path

from FurnitureShop import settings
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('about/', about, name='about'),
    path('products/', product_list, name='products'),
    path('products/<slug:room_slug>', product_list, name='product_list_by_room'),
    path('products/<slug:room_slug>/<slug:category_slug>', product_list, name='product_list_by_category'),
    path('product_detail/<int:id>/<slug:slug>', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
