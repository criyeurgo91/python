from django.db import models

# Create your models here.

class Category (models.Model):
    name           = models.CharField(max_length=100)
    description    = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
class Marca (models.Model):
    name          =models.CharField(max_length=100)

    def __str__ (self):
        return self.name
    
class Product (models.Model):
    name            = models.CharField(max_length=100)
    description     = models.TextField(max_length=500)
    status          = models.BooleanField(default=True)
    price           = models.DecimalField(max_digits=10,decimal_places=2)
    stock           = models.IntegerField()
    categories      = models.ManyToManyField(Category, null=True, blank=True)
    marca           = models.ForeignKey(Marca, on_delete=models.CASCADE)
    image           = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__ (self):
        return self.name
        