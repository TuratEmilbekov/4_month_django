from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    DoesNotExist = None
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text