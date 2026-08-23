from django.urls import path
from . import views

app_name = "portal"
urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.StudentLoginView.as_view(), name="login"),
    path("logout/", views.StudentLogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("upload/", views.upload_document, name="upload"),
    path("document/<int:pk>/download/", views.download_document, name="download_document"),
]