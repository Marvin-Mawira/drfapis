from django.db import models

# Create your models here.

class Item(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
 
    def __str__(self) -> str:
        return self.name