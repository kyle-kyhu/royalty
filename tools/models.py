from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

from datetime import date

class WillpowerTool(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    willpower_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.created_at) + " " + str(self.willpower_rating) + " " + str(self.description)
    
    def get_absolute_url(self):
        return reverse('tools_detail', kwargs={'pk': self.pk})
    
class FlowTool(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flow_rating = models.IntegerField(default=0, choices=[(i, i) for i in range(-2, 3)])
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at) | (self.flow_rating) | str(self.name)

class PressureTool(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    now_pressure_release = models.BooleanField(default=False)
    now_release_description = models.CharField(max_length=255, blank=True)
    later_pressure_release = models.BooleanField(default=False)
    later_release_time = models.DateTimeField()
    later_release_description = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at) | (self.now_pressure_release) | (self.later_pressure_release) | str(self.name)
    
class OneThingTool(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    one_thing_description = models.CharField(max_length=255, blank=True)
    one_thing_time = models.DateField(default=date.today, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at) | (self.one_thing_description) | str(self.name)
 
class ToolsList(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_at) | str(self.name)