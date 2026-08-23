# from django.shortcuts import render

# # Create your views here.
############################################################

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentSignUpForm, DocumentUploadForm
from .models import StudentProfile, DocumentType, StudentDocument


class StudentLoginView(LoginView):
    template_name = "portal/login.html"


class StudentLogoutView(LogoutView):
    pass


def signup(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! Complete your profile to get started.")
            return redirect("portal:dashboard")
    else:
        form = StudentSignUpForm()
    return render(request, "portal/signup.html", {"form": form})


@login_required
def dashboard(request):
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    required_docs = DocumentType.objects.filter(is_required=True)
    uploaded = {d.document_type_id: d for d in profile.documents.all()}
    checklist = [
        {"doc_type": dt, "uploaded_doc": uploaded.get(dt.id)}
        for dt in required_docs
    ]
    return render(request, "portal/dashboard.html", {
        "profile": profile,
        "checklist": checklist,
    })


@login_required
def upload_document(request):
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.student = profile
            doc.save()
            messages.success(request, "Document uploaded — pending review.")
            return redirect("portal:dashboard")
    else:
        form = DocumentUploadForm()
    return render(request, "portal/upload.html", {"form": form})


@login_required
def download_document(request, pk):
    """Owner or staff only — never a guessable public media URL."""
    doc = get_object_or_404(StudentDocument, pk=pk)
    if doc.student.user_id != request.user.id and not request.user.is_staff:
        raise Http404()
    return FileResponse(doc.file.open("rb"), as_attachment=True, filename=doc.file.name.split("/")[-1])