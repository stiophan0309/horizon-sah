from django.conf.urls import url
from .views import commission, commission_success


urlpatterns = [
     url(r'^$', commission, name="commission"),
    url(r'^commission_success/', commission_success, name='commission_success'),
]
