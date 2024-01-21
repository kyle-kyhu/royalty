# Generated by Django 4.2.9 on 2024-01-19 02:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("goals", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goals",
            name="once_a_month",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="goals",
            name="once_a_month_amount",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="goals",
            name="once_a_quarter",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="goals",
            name="once_a_quarter_amount",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="goals",
            name="once_a_year",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="goals",
            name="once_a_year_amount",
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name="goals",
            name="once_every_five_years",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="goals",
            name="once_every_five_years_amount",
            field=models.IntegerField(blank=True),
        ),
    ]
