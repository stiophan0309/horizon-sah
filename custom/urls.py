from django.conf.urls import url
from .views import create_custom

urlpatterns = [
    url(r'^$', create_custom, name="custom"),
]