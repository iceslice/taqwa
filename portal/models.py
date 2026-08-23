# from django.db import models

# # Create your models here.
######################################################

import uuid
from django.conf import settings
from django.db import models
from leads.models import Lead

def student_upload_path(instance, filename):
    ext = filename.split(".")[-1]
    new_name = f"{uuid.uuid4()}.{ext}"
    return f"student_documents/{instance.student.user.id}/{new_name}"


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile")
    lead = models.OneToOneField(Lead, on_delete=models.SET_NULL, null=True, blank=True, related_name="student_profile")
    phone = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    passport_number = models.CharField(max_length=50, blank=True)
    target_country = models.CharField(max_length=100, blank=True)
    application_status = models.CharField(max_length=30, choices=[
        ("profile_created", "Profile Created"),
        ("documents_pending", "Documents Pending"),
        ("documents_submitted", "Documents Submitted"),
        ("under_review", "Under Review"),
        ("application_submitted", "Application Submitted to University"),
        ("offer_received", "Offer Received"),
        ("visa_applied", "Visa Applied"),
        ("visa_approved", "Visa Approved"),
        ("completed", "Completed"),
    ], default="profile_created")

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class DocumentType(models.Model):
    """Admin-configurable checklist item, e.g. 'Passport Copy', 'IELTS Score'."""
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    is_required = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class StudentDocument(models.Model):
    STATUS_CHOICES = [
        ("pending_review", "Pending Review"),
        ("approved", "Approved"),
        ("rejected", "Needs Re-upload"),
    ]
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="documents")
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
    file = models.FileField(upload_to=student_upload_path)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending_review")
    reviewer_comment = models.CharField(max_length=300, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.document_type.name} — {self.student}"