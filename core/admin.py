# from django.contrib import admin

# # Register your models here.
########################################################

from django.contrib import admin
from .models import SiteSettings, StaticPage

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass

@admin.register(StaticPage)
class StaticPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "updated_at")
    prepopulated_fields = {"slug": ("title",)}