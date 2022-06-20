from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import generics

from mainapp.models import Category, Store, Product
from .serializers import CategoryListSerializer, StoreListSerializer, ProductListSerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category


class StoreListView(generics.ListAPIView):
    serializer_class = StoreListSerializer

    def get_queryset(self):
        store = Store.objects.all()
        return store


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        product = Product.objects.filter(category_id=self.kwargs['pk'])

        return product
