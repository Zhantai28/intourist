from django.urls import path
from .views import place, places, create_place, edit_place, delete_place

app_name = 'places'

urlpatterns = [
    path('', places, name='places-list'),
    path('create/', create_place, name="create-place"),
    path('<int:id>/', place, name='place'),
    path('<int:id>/edit/', edit_place, name='edit-place'),
    path('<int:id>/delete/', delete_place, name='delete-place'),
]
