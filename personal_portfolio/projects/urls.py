from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path('home', views.home, name="home"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]