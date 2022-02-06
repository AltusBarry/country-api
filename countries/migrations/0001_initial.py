# Generated by Django 4.0.2 on 2022-02-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "code",
                    models.CharField(
                        help_text="ISO 4217 code.",
                        max_length=3,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("alpha_2_code", models.CharField(max_length=3, unique=True)),
                ("alpha_3_code", models.CharField(max_length=3, unique=True)),
                ("active", models.BooleanField(default=True)),
                ("currencies", models.ManyToManyField(to="countries.Currency")),
            ],
        ),
    ]
