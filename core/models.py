# from django.db import models

# # Create your models here.
#####################################################

from django.db import models

class SiteSettings(models.Model):
    """Singleton-style row for global editable content (phone, address, stats)."""
    phone = models.CharField(max_length=30, blank=True)
    whatsapp_number = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    students_served = models.PositiveIntegerField(default=0)
    visa_success_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    office_hours = models.CharField(max_length=200, blank=True)
    map_embed_url = models.URLField(max_length=2000, blank=True,
    help_text="The src URL from Google Maps → Share → Embed a map")
    map_link = models.URLField(max_length=500, blank=True,
    help_text="Google Maps 'Share' link for the Get Directions button")

    facebook_url = models.URLField(blank=True, help_text="Full URL, e.g. https://facebook.com/taqwaglobaleducation")
    youtube_url = models.URLField(blank=True, help_text="Full URL to your channel")
    instagram_url = models.URLField(blank=True, help_text="Full URL to your Instagram profile")
    linkedin_url = models.URLField(blank=True, help_text="Full URL to your LinkedIn profile")
    x_url = models.URLField(blank=True, help_text="Full URL to your X (Twitter) profile")
    tiktok_url = models.URLField(blank=True, help_text="Full URL to your TikTok profile")

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return "Site Settings"

class StaticPage(models.Model):
    """For About/Privacy/Terms/etc — editable via admin, no redeploy needed."""
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title