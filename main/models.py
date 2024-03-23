from django.db import models

# Create your models here.
class Header(models.Model):
    bg = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    btn = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Card(models.Model):
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    prrce = models.CharField(max_length=500)
    details = models.TextField()

    def __str__(self):
        return self.title