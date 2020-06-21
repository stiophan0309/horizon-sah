from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, 'index.html')


def contact_form(request):
    if request.method=="POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Request submitted")
            return redirect(reverse('request_confirmation'))
    else:
        form = ContactForm()

    return render(request, "index.html#contact", {'form': form})


def request_confirmation(request):
    """A view that displays the index page"""
    return render(request, 'confirmation.html')
