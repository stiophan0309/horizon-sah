from django.conf.urls import url
from .views import create_custom, custom_form
from .views import request_confirmation

urlpatterns = [
    url(r'^$', create_custom, name="custom"),
    url(r'^custom/$', custom_form, name="custom_form"),
    url(r'^custom/$', request_confirmation, name="request_confirmation"),
]