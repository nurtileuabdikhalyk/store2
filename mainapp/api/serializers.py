from rest_framework import serializers

from mainapp.models import Category, Store, Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name")


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name",'update_counter')
