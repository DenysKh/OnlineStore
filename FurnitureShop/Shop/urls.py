from django.conf.urls.static import static
from django.urls import path

from FurnitureShop import settings
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('<slug:room_slug>', product_list, name='product_list_by_room'),
    path('<slug:room_slug>/<slug:category_slug>', product_list, name='product_list_by_category'),
    path('product_detail/<int:id>/<slug:slug>', product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
