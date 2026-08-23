# from django.db import models

# # Create your models here.
######################################################

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    flag_emoji = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class University(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="universities")
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    city = models.CharField(max_length=100)
    ranking = models.PositiveIntegerField(null=True, blank=True)
    tuition_from_usd = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="universities/logos/", blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["ranking", "name"]

    def __str__(self):
        return f"{self.name} ({self.country.name})"