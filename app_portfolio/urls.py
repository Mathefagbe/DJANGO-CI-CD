from .views import HomeView,ProjectView
from django.urls import path

urlpatterns = [
    path("home/",HomeView.as_view()),
    path("project/",ProjectView.as_view(),name="project")
]