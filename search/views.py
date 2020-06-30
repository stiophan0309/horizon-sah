from django.shortcuts import render
from works.models import Work

"""Create a view that performs a search in the gallery"""
def do_search(request):
    works = Work.objects.filter(title__icontains=request.GET['q'])
    return render(request, "works.html", {"works": works})
