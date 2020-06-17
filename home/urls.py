from django.conf.urls import url
from .views import contact

urlpatterns = [
    # url(r'^index/', index, name="index"),
    url(r'^contact/', contact, name="contact"),
]