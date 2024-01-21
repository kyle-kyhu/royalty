from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import WillpowerTool, FlowTool, PressureTool, OneThingTool, ToolsList
from .forms import WillpowerToolForm, FlowToolForm, PressureToolForm, OneThingToolForm, PressureNowForm, PressureLaterForm

# Create your views here.

class ToolsListView(ListView):
    model = ToolsList 
    template_name = 'tools/tools_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome to the home page!'
        return context


class WillpowerToolView(LoginRequiredMixin,CreateView):
    model = WillpowerTool
    form_class = WillpowerToolForm
    template_name = 'tools/willpower.html'
    success_url = reverse_lazy('tools:tools_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WillpowerDetailView(LoginRequiredMixin,CreateView):
    model = WillpowerTool
    form_class = WillpowerToolForm
    template_name = 'tools/willpower_detail.html'
    


class FlowToolView(LoginRequiredMixin, CreateView):
    model = FlowTool
    form_class = FlowToolForm
    template_name = 'tools/flow.html'
    success_url = reverse_lazy('tools:tools_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FlowDetailView(LoginRequiredMixin, UpdateView):
    model = FlowTool
    form_class = FlowToolForm
    template_name = 'tools/flow_detail.html'
    
    

class PressureToolView(LoginRequiredMixin, TemplateView):
    template_name = 'tools/pressure_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now_form'] = PressureNowForm(self.request.POST or None)
        context['later_form'] = PressureLaterForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        now_form = context['now_form']
        later_form = context['later_form']
        if now_form.is_valid():
            now_form.save()
        elif later_form.is_valid():
            later_form.save()
        return self.render_to_response(context)
    
class PressureDetailView(LoginRequiredMixin, UpdateView):
    model = PressureTool
    form_class = PressureToolForm
    template_name = 'tools/pressure_detail.html'


# class OneThingToolView(UpdateView):
#     model = OneThingTool
#     template_name = 'tools/tools_detail.html'
#     form_class = OneThingToolForm


class ToolsDashboardView(ListView):
    model = WillpowerTool, FlowTool, PressureTool, OneThingTool
    template_name = 'tools/tools_dashboard.html'
    context_object_name = 'tools_dashboard'