from django import forms
from .models import Lead, LeadNote

class LeadCaptureForm(forms.ModelForm):
    """Public-facing form — used on Contact / Free Consultation pages."""
    class Meta:
        model = Lead
        fields = [
            "full_name", "email", "phone", "country_of_residence",
            "preferred_destination", "interested_service", "message",
        ]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }

class LeadStatusForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["status", "assigned_to"]

class LeadNoteForm(forms.ModelForm):
    class Meta:
        model = LeadNote
        fields = ["note"]
        widgets = {"note": forms.Textarea(attrs={"rows": 3, "placeholder": "Log a call, email, or update..."})}