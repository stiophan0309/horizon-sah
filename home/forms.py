from django import forms

class ContactForm(forms.Form):
    """Form to allow users to contact site"""
    name = forms.CharField(required=True, max_length=75)
    email = forms.EmailField(required=True, max_length=75)
    subject = forms.CharField(required=True, max_length=75)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=500)

