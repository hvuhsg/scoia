from django.shortcuts import render
from catalog.models import Photo


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_photos = Photo.objects.all().count()
    photos = Photo.objects.all()

    context = {"num_photos": num_photos, "photos": photos}

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
