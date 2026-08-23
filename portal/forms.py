from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile, StudentDocument

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit)
        StudentProfile.objects.create(user=user, phone=self.cleaned_data.get("phone", ""))
        return user


ALLOWED_EXTENSIONS = ["pdf", "jpg", "jpeg", "png"]
MAX_UPLOAD_MB = 8

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = StudentDocument
        fields = ["document_type", "file"]

    def clean_file(self):
        f = self.cleaned_data["file"]
        ext = f.name.rsplit(".", 1)[-1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise forms.ValidationError("Only PDF, JPG, or PNG files are allowed.")
        if f.size > MAX_UPLOAD_MB * 1024 * 1024:
            raise forms.ValidationError(f"File must be under {MAX_UPLOAD_MB}MB.")
        return f