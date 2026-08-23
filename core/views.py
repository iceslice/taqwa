# from django.shortcuts import render

# # Create your views here.
############################################################

from django.shortcuts import render, get_object_or_404
from .models import SiteSettings, StaticPage
from services.models import Service
from universities.models import University

def home(request):
    settings_obj, _ = SiteSettings.objects.get_or_create(pk=1)
    featured_services = Service.objects.filter(is_active=True)[:3]
    featured_universities = University.objects.filter(is_featured=True)[:6]
    return render(request, "core/home.html", {
        "site": settings_obj,
        "services": featured_services,
        "universities": featured_universities,
    })

def about(request):
    page = get_object_or_404(StaticPage, slug="about")
    return render(request, "core/static_page.html", {"page": page})

def static_page(request, slug):
    page = get_object_or_404(StaticPage, slug=slug)
    return render(request, "core/static_page.html", {"page": page})