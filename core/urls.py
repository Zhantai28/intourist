from django.urls import path
from .views import profile, HomeView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
    path('profile/', profile, name="profile")
]
