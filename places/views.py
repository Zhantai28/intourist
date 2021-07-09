from django import forms
from django.shortcuts import render, redirect
from django.views import generic
from .models import Place, Feedback
from .forms import PlaceForm, FeedbackForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

# Create your views here.


def places(request):
    places_objects = Place.objects.all()
    return render(request, 'places/places.html', {'places': places_objects})


def create_place(request):
    if request.method == "POST":
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place_form.save()
            return redirect('/places/')

    place_form = PlaceForm()
    return render(request, "places/form.html", {'place_form': place_form})


def place(request, id):
    place_object = get_object_or_404(Place, pk=id)
    return render(request, 'places/place.html', {'place_object': place_object})


def edit_place(request, id):
    place_object = get_object_or_404(Place, pk=id)

    if request.method == "POST":
        place_form = PlaceForm(data=request.POST, instance=place_object)
        if place_form.is_valid():
            place_form.save()
            return redirect(f'/places/{id}')

    place_form = PlaceForm(instance=place_object)
    return render(request, 'places/form.html', {'place_form': place_form})


def delete_place(request, id):
    place_object = Place.objects.get(id=id)
    place_object.delete()
    return redirect('/places/')


class FeedbackView(generic.FormView):
    template_name = "places/feedback_form.html"
    form_class = FeedbackForm
    success_url = reverse_lazy('places:places-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FeedbackDetailView(generic.DetailView):
    queryset = Feedback.objects.all()
    template_name = "places/feedback.html"
