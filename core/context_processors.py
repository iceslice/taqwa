from .models import SiteSettings
from django.conf import settings

def site_settings(request):
    obj, _ = SiteSettings.objects.get_or_create(pk=1)
    return {
        "site": obj,
        "WHATSAPP_NUMBER": settings.WHATSAPP_NUMBER,
    }