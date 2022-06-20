from django.contrib import admin
from .models import *


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category')
    list_display_links = ('name',)
    search_fields = ('name',)
    readonly_fields = ('update_counter',)
