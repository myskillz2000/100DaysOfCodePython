from django.db import models
from django.forms import URLField


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        choices=CompanyStatus.choices, default=CompanyStatus.HIRING, max_length=20
    )
    last_update = models.DateTimeField(auto_now_add=True, editable=True)
    application_link = models.URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
