from .import views
from django.urls import path

urlpatterns = [
    path("home1/",views.home1, name="home1.html"),
    path("register/",views.register, name="register.html"),
    path("login/",views.login1, name="login.html"),
]