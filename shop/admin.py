from django.contrib import admin
from shop.models import Shop


@admin.register(Shop)
class ContactAdmin(admin.ModelAdmin):

    model = Shop
