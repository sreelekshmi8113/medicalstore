from django.db import models
from django.core.validators import validate_email


#product
class Product(models.Model):
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
