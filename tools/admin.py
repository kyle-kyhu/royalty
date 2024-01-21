from django.contrib import admin
from .models import WillpowerTool, FlowTool, PressureTool, OneThingTool

# Register your models here.
class WillpowerToolAdmin(admin.ModelAdmin):
    list_display = ('willpower_rating', 'description', 'created_at', 'updated_at')

class FlowToolAdmin(admin.ModelAdmin):
    list_display = ('flow_rating', 'description', 'created_at', 'updated_at')

class PressureToolAdmin(admin.ModelAdmin):
    list_display = ('now_pressure_release', 'now_release_description', 'later_pressure_release', 'later_release_time', 'later_release_description', 'description', 'created_at', 'updated_at')

class OneThingToolAdmin(admin.ModelAdmin):
    list_display = ('one_thing_description', 'one_thing_time', 'created_at', 'updated_at')

admin.site.register(WillpowerTool)
admin.site.register(FlowTool)
admin.site.register(PressureTool)
admin.site.register(OneThingTool)

