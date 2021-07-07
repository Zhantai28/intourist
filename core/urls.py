from django.urls import path
from .views import homepage, profile

app_name = 'core'

urlpatterns = [
    path('', homepage, name="homepage"),
    path('profile/', profile, name="profile")
]
