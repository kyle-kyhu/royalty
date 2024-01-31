from django import forms

from .models import PrivateEvent, InviteEvent

class PrivateEventForm(forms.ModelForm):
    class Meta:
        model = PrivateEvent
        fields = (
            'treated_user',
            'description',
            'tier',
            'estimated_amount',
            )
        
class InviteForm(forms.ModelForm):
   class Meta:
       model = InviteEvent
       fields = (
              'email',
              'phone_number',
              'percentage_of_cost',
              'event_amount',
              'accepted'
              )

