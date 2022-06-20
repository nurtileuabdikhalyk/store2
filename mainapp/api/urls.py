from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.StoreListView.as_view()),
    path('categories/', api_views.CategoryListView.as_view()),
    path('categories/<int:pk>/', api_views.ProductListView.as_view()),
]
