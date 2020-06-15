from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=120)
 
    def __str__(self):
        return self.name
 
 
class Commissions(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    product = models.ForeignKey(Product)
    details = models.TextField()
    media = models.BooleanField()
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.customer_name
