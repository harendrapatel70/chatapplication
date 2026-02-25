from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("change-password/", change_password, name="change_password"),
    path('chat/', chat_view, name='chat'),
]
