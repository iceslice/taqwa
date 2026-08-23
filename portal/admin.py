# from django.contrib import admin

# # Register your models here.
########################################################

from django.contrib import admin
from .models import StudentProfile, DocumentType, StudentDocument

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "is_required", "order")
    list_editable = ("is_required", "order")

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "target_country", "application_status")
    list_filter = ("application_status", "target_country")

@admin.register(StudentDocument)
class StudentDocumentAdmin(admin.ModelAdmin):
    list_display = ("student", "document_type", "status", "uploaded_at")
    list_filter = ("status", "document_type")
    list_editable = ("status",)