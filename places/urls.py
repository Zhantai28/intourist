from django.urls import path
from .views import place, places, create_place, edit_place, delete_place, FeedbackView, FeedbackDetailView

app_name = 'places'

urlpatterns = [
    path('', places, name='places-list'),
    path('create/', create_place, name="create-place"),
    path('<int:id>/', place, name='place'),
    path('<int:id>/edit/', edit_place, name='edit-place'),
    path('<int:id>/delete/', delete_place, name='delete-place'),
    path('feedback/', FeedbackView.as_view(), name="feedback"),
    path("feedback/<int:pk>/", FeedbackDetailView.as_view(), name="feedback-detail"),
]
