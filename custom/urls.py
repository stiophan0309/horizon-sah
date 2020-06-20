from django.conf.urls import url
from .views import create_custom
from .views import request_confirmation

urlpatterns = [
    url(r'^$', create_custom, name="custom"),
    url(r'^$', request_confirmation, name="request_confirmation"),
]