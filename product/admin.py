from django.contrib import admin
from product.models import Product, Category, ProductInfo, Parameter, ProductParameter


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    model = Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    model = Product


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):

    model = ProductInfo
    list_display = ('product', 'model', 'shop')


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):

    model = Parameter


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):

    model = ProductParameter
