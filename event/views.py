from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PrivateEvent, InviteEvent
from .forms import PrivateEventForm, InviteForm

# Create your views here.

class PrivateEventListView(LoginRequiredMixin, ListView):
    '''List all private events'''
    template_name = "events/private_event_list.html"
    model = PrivateEvent
    context_object_name = 'private_events'


    
class PrivateEventCreateView(LoginRequiredMixin, CreateView):
    '''Create a private event'''
    template_name = "events/private_event_add.html"
    model = PrivateEvent
    form_class = PrivateEventForm
    success_url = reverse_lazy('events:private_event_list')
    
    def form_valid(self, form):
        form.instance.point_of_contact = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('events:invite_private_event', kwargs={'pk': self.object.pk})
    
class PrivateEventInviteView(LoginRequiredMixin, UpdateView):
    '''Create an invite to a private event'''
    template_name = "events/invite_private_event.html"
    model = InviteEvent  
    form_class = InviteForm
    success_url = reverse_lazy('events:private_event_list')
    
    def form_valid(self, form):
        form.instance.point_of_contact = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('events:private_event_list')
    
class PrivateEventDetailView(LoginRequiredMixin,DetailView):
    model = PrivateEvent
    template_name = "events/private_event_detail.html"
    context_object_name = 'private_event' #what is this?

class MethodOfPaymentView(TemplateView):
    model = PrivateEvent
    template_name = "events/method_of_payment.html"
    context_object_name = 'private_event'
    
