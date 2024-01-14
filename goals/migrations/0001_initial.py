# Generated by Django 4.2.9 on 2024-01-14 03:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Goals",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("once_a_month", models.CharField(max_length=255)),
                ("once_a_month_amount", models.IntegerField()),
                ("once_a_quarter", models.CharField(max_length=255)),
                ("once_a_quarter_amount", models.IntegerField()),
                ("once_a_year", models.CharField(max_length=255)),
                ("once_a_year_amount", models.IntegerField()),
                ("once_every_five_years", models.CharField(max_length=255)),
                ("once_every_five_years_amount", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
