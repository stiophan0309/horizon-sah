from django.conf.urls import url, include
from .views import all_works

urlpatterns = [
    url(r'^$', all_works, name='works'),
]