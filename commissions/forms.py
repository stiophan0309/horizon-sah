from django import forms

class CommissionsForm(forms.Form):
    name = forms.CharField(max_length=254)
    email = forms.EmailField(max_length=254)
    description = forms.Textarea()
    media = forms.CharField(max_length=254)
    surface = forms.CharField(max_length=254)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
