from django.conf.urls import url
from .views import contact_form
from .views import request_confirmation

urlpatterns = [
    url(r'^$', contact_form, name="contact"),
    url(r'^$', request_confirmation, name="request_confirmation"),
]