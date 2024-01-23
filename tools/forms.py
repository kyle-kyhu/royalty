from django import forms
from .models import WillpowerTool, FlowTool, PressureTool, OneThingTool


class WillpowerToolForm(forms.ModelForm):
    class Meta:
        model = WillpowerTool
        fields = ('willpower_rating', 'description',)


class FlowToolForm(forms.ModelForm):
    class Meta:
        model = FlowTool
        fields = ('flow_rating', 'description',)

        widgets = {"description": forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter willpower driver here",
                })}


class PressureToolForm(forms.ModelForm):
    class Meta:
        model = PressureTool
        fields = (
            'now_pressure_release', 
            'later_pressure_release', 
            )

class PressureNowForm(forms.ModelForm):
    class Meta:
        model = PressureTool
        fields = (
            'now_release_description', 
            )

class PressureLaterForm(forms.ModelForm):
    class Meta:
        model = PressureTool
        fields = (
            'later_release_time',
            'later_release_description', 
            ) 

        
class OneThingToolForm(forms.ModelForm):
    class Meta:
        model = OneThingTool
        fields = ('one_thing_description', 'one_thing_time',)
    
