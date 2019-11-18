from django.db import models
from category.models import Category

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return f'{self.title} Category: {self.category}'