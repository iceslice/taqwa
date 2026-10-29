# from django.shortcuts import render

# # Create your views here.
############################################################

from django.shortcuts import render, get_object_or_404
from .models import SiteSettings, StaticPage
from services.models import Service
from universities.models import University
###################
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from leads.forms import LeadCaptureForm
from leads.views import _notify_staff_new_lead

def contact(request):
    site, _created = SiteSettings.objects.get_or_create(pk=1)
    if request.method == "POST":
        form = LeadCaptureForm(request.POST)
        if form.is_valid():
            lead = form.save()
            _notify_staff_new_lead(lead)
            messages.success(request, _("Thanks! Our team will contact you within 24 hours."))
            return redirect("core:contact")
    else:
        form = LeadCaptureForm()
    return render(request, "core/contact.html", {"site": site, "form": form})
######################

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