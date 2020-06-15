from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Commissions
from .forms import CommissionsForm

# Create your views here.
def sendView(request):
    if request.method == 'GET':
        form = CommissionsForm()
    else:
        form = CommissionsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            try:
                send_mail(name, email, description, ['steven.a.horne@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Your request was sent.')
