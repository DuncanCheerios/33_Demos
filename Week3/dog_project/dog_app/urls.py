from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_dogs, name="all_dogs"),
    path("<str:dog_name>/", views.view_dog, name="dog_view"),
]

