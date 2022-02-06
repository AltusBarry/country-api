from django.db import models
from django.core.validators import MaxValueValidator


class Currency(models.Model):
    """Light weight currency model.
    Missing much of the expected currency data. We do not need any of that for
    this assessment project.
    """

    code = models.CharField(
        primary_key=True,
        max_length=3,
        help_text="ISO 4217 alpha code.",
    )
    name = models.CharField(max_length=100)

    # unique_together = [["code", "numeric_code"]]


class CountryActiveManager(models.Manager):
    """Django queryset manager that filters inactive countries out by default."""

    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Country(models.Model):
    """Light weight country model.
    Deals only with some of the data for a top level territory as defined in
    the ISO 3166-1 spec.
    """

    name = models.CharField(max_length=100)
    alpha_2_code = models.CharField(
        max_length=3, unique=True, help_text="ISO 3166-1 Alpha 2 code."
    )
    alpha_3_code = models.CharField(
        max_length=3, unique=True, help_text="ISO 3166-1 Alpha 3 code."
    )
    currencies = models.ManyToManyField("Currency")
    active = models.BooleanField(default=True)
    objects = CountryActiveManager()
