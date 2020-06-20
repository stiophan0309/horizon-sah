from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .models import Custom
from .forms import CustomForm


@login_required()
def create_custom(request):
    if request.method=="POST":
        form = CustomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('request_confirmation'))
    else:
        form = CustomForm()

    return render(request, "custom.html", {'form': form})


def request_confirmation(request):
    """A view that displays the index page"""
    return render(request, 'confirmation.html')
