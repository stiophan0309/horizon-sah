from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Custom
from .forms import CustomForm

@login_required()
def create_custom(request):
    return render(request, "custom.html")

@login_required()
def custom_form(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Request submitted")
            return redirect(reverse('request_confirmation'))
    else:
        form = CustomForm()

    return render(request, "custom_form.html", {'form': form})

@login_required()
def request_confirmation(request):
    """ Confirmation message """
    return render(request, 'confirmation.html')
