from django.db import models
from django.utils import timezone

# Create your models here.
class Work(models.Model):

    title = models.CharField(max_length=30, blank=False)
    category = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to="images", blank=True, null=False)
    surface = models.CharField(max_length=30, blank=False, default='')
    media = models.CharField(max_length=30, blank=False, default='')
    date = models.DateTimeField(blank=True, null=True, default='date unknown')
    hsize = models.IntegerField(blank=False, null=False, default=0)
    vsize = models.IntegerField(blank=False, null=False, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)

    def __str__(self):
        return self.name
