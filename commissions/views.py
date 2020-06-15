from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CommissionsForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def commission(request):
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
            return render(request, "commissions.html", {'form': form})

def commission_success(request):
    return HttpResponse('Success! Your request was sent.')
