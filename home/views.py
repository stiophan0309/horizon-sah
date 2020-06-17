from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")

def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")

def contact(request):
    """View handle contact form requests"""
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            message = request.POST['message']
            subject = request.POST['subject']
            send_mail(
                subject,
                "Message from: " +
                request.POST['email'] +
                "Message: " +
                message,
                'xxx',
                ['steven.a.horne@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!",
                                      extra_tags="alert-success")
            return redirect(reverse('index'))
        else:
            messages.error(request, "Unable to send message at this time",
                                    extra_tags="alert-danger")
    else:
        contact_form = ContactForm()
    return render(request, 'index.html#contact', {'contact_form': contact_form})
