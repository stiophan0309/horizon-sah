from django.conf.urls import url, include
from accounts import url_reset
from .views import (register, profile, logout, login, edit_profile,
                    delete_profile)

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', profile, name="profile"),
    url(r'^edit/$', edit_profile, name='edit_profile'),
    url(r'^delete/$', delete_profile, name='delete_profile'),
    url(r'^password-reset/', include(url_reset))
]