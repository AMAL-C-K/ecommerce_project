from django.contrib import admin

from ecom_app.models import Category, Brands, Products


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('brand_name',)}


admin.site.register(Brands, BrandAdmin)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'price', 'category', 'brand', 'image', 'stock', 'available', 'trending',
                    'offer']
    list_editable = ['base_price', 'price', 'image', 'stock', 'available', 'trending', 'offer']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products, ProductsAdmin)