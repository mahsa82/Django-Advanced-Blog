from django.urls import path, include
from .. import views


urlpatterns = [
    # Profile
    path("profile/", views.ProfileAPIView.as_view(), name="Profile"),
]
