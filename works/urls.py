from django.conf.urls import url
from .views import all_works

urlpatterns = [
    url(r'^works/', all_works, name="works")
]