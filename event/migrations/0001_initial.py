# Generated by Django 4.2.9 on 2024-01-29 15:28

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
            name="PrivateEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("treated_user", models.CharField(max_length=155)),
                ("description", models.TextField()),
                ("tier", models.IntegerField()),
                ("estimated_amount", models.IntegerField()),
                (
                    "point_of_contact",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "permissions": (
                    ("cannot_view_private_event", "Cannot view private event"),
                    ("can_edit_private_event", "Can edit private event"),
                ),
            },
        ),
        migrations.CreateModel(
            name="InviteEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=15)),
                ("accepted", models.BooleanField(default=False)),
                ("percentage_of_cost", models.IntegerField()),
                ("event_amount", models.IntegerField()),
                (
                    "private_event",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="event.privateevent"),
                ),
            ],
        ),
    ]
