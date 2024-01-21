from django.urls import path
from tools.views import (
    ToolsListView,
    ToolsDashboardView, 
    WillpowerToolView,
    WillpowerDetailView,
    FlowToolView,
    FlowDetailView,
    PressureToolView,
    PressureDetailView

)

app_name = "tools"
urlpatterns = [
    path("", ToolsListView.as_view(), name="tools_list"),
    path("willpower/", WillpowerToolView.as_view(), name="willpower"),
    path("willpower/<int:pk>/", WillpowerDetailView.as_view(), name="willpower_detail"),
    path("flow/", FlowToolView.as_view(), name="flow"),
    path("flow/<int:pk>/", FlowDetailView.as_view(), name="flow_detail"),
    path("pressure/", PressureToolView.as_view(), name="pressure"),
    path("pressure/<int:pk>/", PressureDetailView.as_view(), name="pressure_detail"),
    path("dashboard/", ToolsDashboardView.as_view(), name="tools_dashboard"),
]

    