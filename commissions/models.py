from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ('new','NEW'),
    ('pending', 'PENDING'),
    ('in progress','IN PROGRESS'),
    ('complete','COMPLETE'),
)

MEDIA_CHOICES = (
    ('pastel', 'PASTEL'),
    ('acrylic', 'ACRYLIC'),
    ('oil','OIL'),
    ('other','OTHER'),
)

SURFACE_CHOICES = (
    ('paper','PAPER'),
    ('canvas', 'CANVAS'),
    ('canvas board','CANVAS BOARD'),
    ('other','OTHER'),
)

class Item(models.Model):

    name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    date = models.DateField(auto_now=True, auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    media = models.CharField(max_length=10, choices=MEDIA_CHOICES, default='pastel')
    surface = models.CharField(max_length=10, choices=SURFACE_CHOICES, default='paper')
    size = models.CharField(max_length=30, blank=False)
    details = models.TextField(blank=False)

    def __str__(self):
        """ makes readable description in admin panel """
        return self.name
