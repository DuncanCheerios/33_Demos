from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_dogs, name="index"),
    path("dog/<str:dog_name>/", views.view_dog, name="dog_view"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
]

