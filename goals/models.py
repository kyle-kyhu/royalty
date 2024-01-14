from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User


class Goals(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    once_a_month = models.CharField(max_length=255)
    once_a_month_amount = models.IntegerField()
    once_a_quarter = models.CharField(max_length=255)
    once_a_quarter_amount = models.IntegerField()
    once_a_year = models.CharField(max_length=255)
    once_a_year_amount = models.IntegerField()
    once_every_five_years = models.CharField(max_length=255)
    once_every_five_years_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.created_at)
    
    def get_absolute_url(self):
        return reverse('goals_detail', kwargs={'pk': self.pk})