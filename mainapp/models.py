from django.db import models
from django.db.models import F


class Store(models.Model):
    name = models.CharField("Название магазина", max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Название категории", max_length=255)
    store = models.ManyToManyField(Store, verbose_name="Магазин")

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField("Имя товара", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    update_counter = models.IntegerField("Количество обновленией", default=0)
    store = models.ManyToManyField(Store, verbose_name="Магазин")

    def counter(self, pk):
        self.filter(id=pk).update(update_counter=F('update_counter') + 1)

    def __str__(self):
        return f"{self.category} - {self.name}"
