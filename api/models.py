from django.db import models
from djongo import models
from rest_framework import generics
from rest_framework import filters

class Data(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name       

class Items(models.Model):
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    in_stock = models.IntegerField()
    available_stock = models.IntegerField()

    def __str__(self):
        return self.name  
