from django.contrib import admin
from .models import Order, OrderPickup, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)


class OrderPickupAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number',
                    'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(OrderPickup, OrderPickupAdmin)
