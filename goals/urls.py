from django.urls import path
from goals.views import GoalsPageView, GoalsDetailView

app_name = "goals"
urlpatterns = [
    path("", GoalsPageView.as_view(), name="goals"),
    path("goals/<int:pk>/", GoalsDetailView.as_view(), name="goals_detail"),
]