from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.models import User

dogs_info = {
    "Fido": {
        "dog_name": "Fido", 
        "dog_age": 3, 
        "dog_favorites": ["walks"],
        "dog_summary": "Fido is a playful young dog that likes to run and fetch"
    },
    "Lassie": {
        "dog_name": "Lassie", 
        "dog_age": 5, 
        "dog_favorites": ["bones"],
        "dog_summary": "Lassie is a loyal companion.  Smart and cheerful."
    },
    "Snoopy": {
        "dog_name": "Snoopy", 
        "dog_age": 9, 
        "dog_favorites": ["naps"],
        "dog_summary": "Snoopy likes to nap in the sun and is very affectionate."
    }
}

# Create your views here.
def view_dog(request, dog_name):
    
    # Get Dog is possible
    if dog_name in dogs_info:
       context = dogs_info[dog_name]
       return render(request, "dog_app/dog_view.html", context)
    else: 
        return redirect("all_dogs")

    
def all_dogs(request):

    # Collect data about the dogs
    dog_names = dogs_info.keys()

    # Pass that data to the template

    return render(request, "dog_app/all_dogs.html", {"dog_names": dog_names})
    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auth/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auth/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auth/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auth/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auth/register.html")
