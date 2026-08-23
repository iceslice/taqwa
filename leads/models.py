# from django.db import models

# # Create your models here.
######################################################

from django.conf import settings
from django.db import models
from django.urls import reverse

class Lead(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("qualified", "Qualified"),
        ("consultation_booked", "Consultation Booked"),
        ("application_started", "Application Started"),
        ("visa_processing", "Visa Processing"),
        ("won", "Won — Enrolled"),
        ("lost", "Lost"),
    ]
    SOURCE_CHOICES = [
        ("website", "Website Form"),
        ("whatsapp", "WhatsApp"),
        ("facebook", "Facebook"),
        ("referral", "Referral"),
        ("walk_in", "Walk-in"),
        ("other", "Other"),
    ]
    DESTINATION_CHOICES = [
        ("uk", "United Kingdom"), ("usa", "USA"), ("canada", "Canada"),
        ("australia", "Australia"), ("malaysia", "Malaysia"),
        ("other", "Other"),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    country_of_residence = models.CharField(max_length=100, blank=True)
    preferred_destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES, blank=True)
    interested_service = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)

    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="website")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="new")
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="assigned_leads"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} ({self.get_status_display()})"

    def get_absolute_url(self):
        return reverse("leads:crm_detail", args=[self.pk])


class LeadNote(models.Model):
    """Internal notes / call logs / follow-up history on a lead — the CRM timeline."""
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="notes")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Note on {self.lead.full_name} @ {self.created_at:%Y-%m-%d}"


class Consultation(models.Model):
    """A booked appointment tied to a lead."""
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="consultations")
    scheduled_for = models.DateTimeField()
    mode = models.CharField(max_length=20, choices=[("phone", "Phone"), ("video", "Video"), ("in_person", "In person")], default="phone")
    counselor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["scheduled_for"]

    def __str__(self):
        return f"Consultation: {self.lead.full_name} @ {self.scheduled_for:%Y-%m-%d %H:%M}"