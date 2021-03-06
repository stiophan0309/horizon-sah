from django.db import models
from django.utils import timezone

# Create your models here.
STATUS_CHOICES = (
    ('new', 'NEW'),
    ('pending', 'PENDING'),
    ('in progress', 'IN PROGRESS'),
    ('complete', 'COMPLETE'),
)

MEDIA_CHOICES = (
    ('pastel', 'PASTEL'),
    ('acrylic', 'ACRYLIC'),
    ('oil', 'OIL'),
    ('other', 'OTHER'),
)

SURFACE_CHOICES = (
    ('paper', 'PAPER'),
    ('canvas', 'CANVAS'),
    ('canvas board', 'CANVAS BOARD'),
    ('other', 'OTHER'),
)

class Custom(models.Model):

    name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    media = models.CharField(max_length=20, choices=MEDIA_CHOICES, default='pastel')
    surface = models.CharField(max_length=20, choices=SURFACE_CHOICES, default='paper')
    size = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    details = models.TextField(blank=False)

    def __unicode__(self):
        """ makes readable description in admin panel """
        return self.name
