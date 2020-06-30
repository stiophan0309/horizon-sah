from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create your views here.
def index(request):
    """A view that displays the index and about pages"""
    return render(request, 'index.html')


def contact(request):
    """A view that displays the contact page"""
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Request submitted")
            return redirect(reverse('contact'))
    else:
        form = ContactForm()

    return render(request, "contact.html", {'form': form})
