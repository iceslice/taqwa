# from django.shortcuts import render

# # Create your views here.
############################################################

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q

from .models import Lead
from .forms import LeadCaptureForm, LeadStatusForm, LeadNoteForm


def capture_lead(request):
    """Public form: homepage 'Free Consultation' / Contact page."""
    if request.method == "POST":
        form = LeadCaptureForm(request.POST)
        if form.is_valid():
            lead = form.save()
            _notify_staff_new_lead(lead)
            messages.success(request, "Thanks! Our team will contact you within 24 hours.")
            return redirect("core:home")
    else:
        form = LeadCaptureForm()
    return render(request, "leads/capture_form.html", {"form": form})


# def _notify_staff_new_lead(lead):
#     if settings.EMAIL_HOST_USER:
#         send_mail(
#             subject=f"New lead: {lead.full_name}",
#             message=f"New consultation request from {lead.full_name} ({lead.phone}, {lead.email}).\n\n{lead.message}",
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[settings.EMAIL_HOST_USER],
#             fail_silently=True,
#         )

def _notify_staff_new_lead(lead):
    if settings.EMAIL_HOST_USER:
        send_mail(
            subject=f"New lead: {lead.full_name}",
            message=f"New consultation request from {lead.full_name} ({lead.phone}, {lead.email}).\n\n"
                    f"Destination: {lead.get_preferred_destination_display() or '—'}\n"
                    f"Service interest: {lead.interested_service or '—'}\n\n"
                    f"Message:\n{lead.message or '—'}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.LEAD_NOTIFICATION_EMAIL],
            fail_silently=True,
        )


@login_required
@permission_required("leads.view_lead", raise_exception=True)
def crm_dashboard(request):
    """Staff pipeline board grouped by status."""
    status_filter = request.GET.get("status")
    qs = Lead.objects.select_related("assigned_to")
    if status_filter:
        qs = qs.filter(status=status_filter)
    q = request.GET.get("q")
    if q:
        qs = qs.filter(Q(full_name__icontains=q) | Q(email__icontains=q) | Q(phone__icontains=q))

    counts = Lead.objects.values("status").annotate(total=Count("id"))
    return render(request, "leads/crm_dashboard.html", {
        "leads": qs[:200],
        "counts": {c["status"]: c["total"] for c in counts},
        "status_choices": Lead.STATUS_CHOICES,
    })


@login_required
@permission_required("leads.change_lead", raise_exception=True)
def crm_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    status_form = LeadStatusForm(instance=lead)
    note_form = LeadNoteForm()

    if request.method == "POST":
        if "update_status" in request.POST:
            status_form = LeadStatusForm(request.POST, instance=lead)
            if status_form.is_valid():
                status_form.save()
                messages.success(request, "Lead updated.")
                return redirect("leads:crm_detail", pk=lead.pk)
        elif "add_note" in request.POST:
            note_form = LeadNoteForm(request.POST)
            if note_form.is_valid():
                note = note_form.save(commit=False)
                note.lead = lead
                note.author = request.user
                note.save()
                return redirect("leads:crm_detail", pk=lead.pk)

    return render(request, "leads/crm_detail.html", {
        "lead": lead,
        "status_form": status_form,
        "note_form": note_form,
        "notes": lead.notes.select_related("author"),
        "consultations": lead.consultations.all(),
    })