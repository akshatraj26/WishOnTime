from django.urls import path, include
from .views import login_user, logout_user, register, home

urlpatterns = [
    path("", home, name='home'),
    path("login_user/", login_user, name='login'),
    path("logout_user/", logout_user, name='logout'),
    path("register_user/", register, name='signup'),
    
]
