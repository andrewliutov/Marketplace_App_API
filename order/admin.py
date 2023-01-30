from django.contrib import admin
from django.db import models
from order.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    models = Order
    list_display = ('user', 'dt')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    models = OrderItem
    list_display = ('order', 'product_info')
