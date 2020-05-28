from django.urls import path, include
from accounts.views import logout, login, registration, user_profile
from accounts import urls_reset

urlpatterns = [
    path('accounts/', index, name="index"),
    path('accounts/logout/', logout, name="logout"),
    path('accounts/login/', login, name="login"),
    path('accounts/registration/', registration, name="registration"),
    path('accounts/user_profile/', user_profile, name="user_profile"),
    path('accounts/password_reset/', include(urls_reset))
]