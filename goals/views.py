from django.urls import reverse
from django.views.generic.edit import FormView, UpdateView


from .models import Goals
from .forms import GoalsForm


class GoalsPageView(FormView):
    template_name = "goals/goals.html"
    model = Goals
    form_class = GoalsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')


class GoalsUpdateView(UpdateView):
    model = Goals
    template_name = "goals/goals_update.html"
    form_class = GoalsForm
    context_object_name = 'object'

    def get_success_url(self):
        return reverse('home')