from django.shortcuts import redirect, render
from django.http import HttpResponse


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
       return render(request, "dog_view.html", context)
    else: 
        return redirect("all_dogs")

    
def all_dogs(request):

    # Collect data about the dogs
    dog_names = dogs_info.keys()

    # Pass that data to the template

    return render(request, "all_dogs.html", {"dog_names": dog_names})