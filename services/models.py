# from django.db import models

# # Create your models here.
#################################################

from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ("study_abroad", "Study Abroad"),
        ("visa", "Visa Support"),
        ("scholarship", "Scholarship"),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=300)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="e.g. bootstrap icon class")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title