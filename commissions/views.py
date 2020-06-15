from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommissionsForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def commissions_form(request):
    if request.method == 'POST':
        form = CommissionsForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'commissions.html')
    else:
        form = CommissionsForm()
    return render(request, 'commissions.html', {'form': form})
