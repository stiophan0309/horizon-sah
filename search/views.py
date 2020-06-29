from django.shortcuts import render
from works.models import Work

# Create your views here.
def do_search(request):
    works = Work.objects.filter(title__icontains=request.GET['q'])
    return render(request, "works.html", {"works": works})
