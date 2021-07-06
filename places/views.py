from django.shortcuts import render, HttpResponse
from .models import Place

# Create your views here.


def places(request):
    places_objects = Place.objects.all()
    return render(request, 'places/places.html', {'places': places_objects})
