from django.urls import path
from goals.views import GoalsPageView, GoalsUpdateView

app_name = "goals"
urlpatterns = [
    path("", GoalsPageView.as_view(), name="goals"),
    path("goals/<int:pk>/", GoalsUpdateView.as_view(), name="goals_update"),
]