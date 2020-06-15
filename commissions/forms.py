from django import forms
from .models import Commissions

class CommissionsForm(forms.ModelForm):

    class Meta:
        model = Commissions
        fields = ('name', 'email', 'description', 'media', 'surface', 'price', 'image')
