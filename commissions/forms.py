from django import forms
from .models import Commissions

class CommissionsForm(forms.ModelForm):
    class Meta:
        model = Commissions
        exclude = []
