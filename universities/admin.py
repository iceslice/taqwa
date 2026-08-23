# from django.contrib import admin

# # Register your models here.
###############################################

# universities/admin.py
from django.contrib import admin
from .models import Country, University

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "flag_emoji")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "city", "ranking", "is_featured")
    list_filter = ("country", "is_featured")
    list_editable = ("is_featured",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "city")