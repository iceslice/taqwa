from django.urls import path
from . import views

app_name = "leads"
urlpatterns = [
    path("apply/", views.capture_lead, name="capture"),
    path("crm/", views.crm_dashboard, name="crm_dashboard"),
    path("crm/<int:pk>/", views.crm_detail, name="crm_detail"),
]