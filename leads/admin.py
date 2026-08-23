# from django.contrib import admin

# # Register your models here.
########################################################

from django.contrib import admin
from .models import Lead, LeadNote, Consultation

class LeadNoteInline(admin.TabularInline):
    model = LeadNote
    extra = 1
    readonly_fields = ("author", "created_at")

class ConsultationInline(admin.TabularInline):
    model = Consultation
    extra = 0

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "status", "source", "assigned_to", "created_at")
    list_filter = ("status", "source", "preferred_destination", "assigned_to")
    search_fields = ("full_name", "email", "phone")
    inlines = [LeadNoteInline, ConsultationInline]
    list_editable = ("status", "assigned_to")