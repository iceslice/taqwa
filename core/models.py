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