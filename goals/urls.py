from django.urls import path
from goals.views import GoalsAddView, GoalsUpdateView, GoalsDeleteView, GoalsListView

app_name = "goals"
urlpatterns = [
    path("", GoalsListView.as_view(), name="goals_list"),
    path("new/", GoalsAddView.as_view(), name="goals_add"),
    path("<int:pk>/", GoalsUpdateView.as_view(), name="goals_edit"),
    path("<int:pk>/delete/", GoalsDeleteView.as_view(), name="goals_delete"),
]