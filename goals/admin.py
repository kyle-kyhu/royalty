from django.contrib import admin
from .models import Goals

class GoalsInline(admin.StackedInline):
    model = Goals
    

admin.site.register(Goals)


