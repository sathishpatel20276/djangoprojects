from django.urls import path
from RegLogApp import views
app_name = "RegLogApp"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
]