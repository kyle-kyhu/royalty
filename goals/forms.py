from django import forms

from .models import Goals

class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = (
            'once_a_month',
            'once_a_month_amount',
            'once_a_quarter',
            'once_a_quarter_amount',
            'once_a_year', 
            'once_a_year_amount', 
            'once_every_five_years', 
            'once_every_five_years_amount',
            )
        widgets = {
            "once_a_month": forms.Textarea(attrs={"class": "form-control","placeholder": "Enter what you want to do once a month",}),
            "once a quarter": forms.Textarea(attrs={"class": "form-control","placeholder": "Enter what you want to do once a quarter",}),
            "once a year": forms.Textarea(attrs={"class": "form-control","placeholder": "Enter what you want to do once a year",}),
            "once every five years": forms.Textarea(attrs={"class": "form-control","placeholder": "Enter what you want to do once every five years",}),
        }