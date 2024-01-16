
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from .models import Goals
from .forms import GoalsForm


class GoalsAddView(LoginRequiredMixin,CreateView):
    '''Add a new goal'''
    template_name = "goals/goals_add.html"
    model = Goals
    form_class = GoalsForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')

class GoalsListView(LoginRequiredMixin, ListView):
    '''List all goals'''
    model = Goals
    template_name = "goals/goals_list.html"
    context_object_name = 'goals'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Goals.objects.filter(user=self.request.user).order_by('-created_at')
        else:
            return Goals.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal'] = context['object_list'].first() if context['object_list'] else None
        return context
    


class GoalsUpdateView(LoginRequiredMixin, UpdateView):
    '''edit goals'''
    model = Goals
    template_name = "goals/goals_edit.html"
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = Goals.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('goals:goals_edit', kwargs={'pk': self.object.pk})
    
class GoalsDeleteView(LoginRequiredMixin, DeleteView):
    '''delete goals'''
    model = Goals
    template_name = "goals/goals_delete.html"
    context_object_name = 'goals'
    
    def get_success_url(self):
        return reverse('goals:goals_list')

    