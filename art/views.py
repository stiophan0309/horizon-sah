from django.shortcuts import render, HttpResponse

# Create your views here.
def get_art(request):
    return render(request, "art.html")
