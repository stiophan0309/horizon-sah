from django.conf.urls import url
from .views import sendView, successView

urlpatterns = [
    url(r'^$', sendView, name='send'),
    url(r'^$', successView, name='success'),
]