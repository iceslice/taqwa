# from django.contrib import admin

# # Register your models here.
###############################################

from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active", "order")
    list_filter = ("category", "is_active")
    list_editable = ("is_active", "order")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary")