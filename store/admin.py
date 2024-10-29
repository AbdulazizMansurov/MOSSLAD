from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "pk")

    def get_count_of_products(self, obj):
        if obj.products:
            return str(len(obj.products.all()))
        else:
            return str(0)

    get_count_of_products.short_description = "Количество продуктов"

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_published', 'category')