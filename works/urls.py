from django.conf.urls import url
from .views import all_works

urlpatterns = [
    url(r'^$', all_works, name='all_works'),
]