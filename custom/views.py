from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Custom
from .forms import CustomForm

def create_custom(request):
    if request.method=="POST":
        form = CustomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(create_custom)
    else:
        form = CustomForm()

    return render(request, "custom.html", {'form': form})
