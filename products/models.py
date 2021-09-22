from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    inStock = models.BooleanField()
    image = models.CharField(max_length=1000)





