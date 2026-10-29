from modeltranslation.translator import register, TranslationOptions
from services.models import Service
from universities.models import University, Country
# from core.models import StaticPage
from core.models import SiteSettings, StaticPage

@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ("address", "office_hours")
    
@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("title", "summary", "description")

@register(University)
class UniversityTranslationOptions(TranslationOptions):
    fields = ("description",)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(StaticPage)
class StaticPageTranslationOptions(TranslationOptions):
    fields = ("title", "body")