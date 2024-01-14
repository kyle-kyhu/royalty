from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView, UpdateView

from .models import Goals
from .forms import GoalsForm

# your stuff

class GoalsPageView(FormView):
    template_name = "goals/goals.html"
    model = Goals
    form_class = GoalsForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class GoalsDetailView(UpdateView):
    model = Goals
    template_name = "goals/goals_detail.html"
    form_class = GoalsForm

    def get_success_url(self):
        return reverse('users:goals_detail', kwargs={'pk': self.object.pk})