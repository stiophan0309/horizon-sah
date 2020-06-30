from django.shortcuts import render
from .models import Work

"""Render the Gallery/Shop"""
def all_works(request):
    works = Work.objects.all()
    return render(request, "works.html", {'works': works})
