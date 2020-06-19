from django import forms
from .models import Custom


class CustomForm(forms.ModelForm):

    class Meta:
        model = Custom
        fields = ('name', 'email', 'date', 'status', 'media', 'surface', 'size', 'image', 'details')
