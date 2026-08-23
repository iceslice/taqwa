from django.urls import path
from . import views

app_name = "universities"
urlpatterns = [
    path("", views.directory, name="directory"),
    path("<slug:slug>/", views.university_detail, name="detail"),
]