from typing import Any
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Goals
from .forms import GoalsForm


class GoalsAddView(CreateView):
    '''Add a new goal'''
    template_name = "goals/goals_add.html"
    model = Goals
    form_class = GoalsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')

class GoalsListView(ListView):
    '''List all goals'''
    model = Goals
    template_name = "goals/goals_list.html"
    context_object_name = 'goals'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Goals.objects.filter(user=self.request.user)
        else:
            return Goals.objects.none()


class GoalsUpdateView(UpdateView):
    '''edit goals'''
    model = Goals
    template_name = "goals/goals_edit.html"
    fields = (
        '__all__',
        # individual fields
        # 'once_a_month',
        # 'once_a_month_amount',
        # 'once_a_quarter',
        # 'once_a_quarter_amount',
        # 'once_a_year',
        # 'once_a_year_amount',
        # 'once_every_five_years',
        # 'once_every_five_years_amount',
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goals'] = Goals.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('goals:goals_edit', kwargs={'pk': self.object.pk})
    
class GoalsDeleteView(DeleteView):
    '''delete goals'''
    model = Goals
    template_name = "goals/goals_delete.html"
    context_object_name = 'goals'
    
    def get_success_url(self):
        return reverse('goals:goals_list')

    