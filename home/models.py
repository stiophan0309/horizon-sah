from django.db import models
from django.utils import timezone

# Create your models here.

SUBJECT_CHOICES = (
    ('general', 'General'),
    ('commission', 'Commission'),
    ('feedback', 'Feedback'),
    ('other', 'Other'),
)

class Contact(models.Model):

    name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='General')
    message = models.TextField(blank=False)

    def __unicode__(self):
        """ makes readable description in admin panel """
        return self.name

