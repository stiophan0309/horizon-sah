from django.conf.urls import url, include
from accounts import url_reset
from .views import (index, register, profile, logout, login, edit_profile,
                    delete_profile, orders)

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', profile, name="profile"),
    url(r'^orders/$', orders, name='orders'),
    url(r'^profile/edit/$', edit_profile, name='edit_profile'),
    url(r'^profile/delete/$', delete_profile, name='delete_profile'),
    url(r'^password-reset/', include(url_reset))
]