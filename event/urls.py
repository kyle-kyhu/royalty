from django.urls import path
from .views import (
    PrivateEventListView, 
    PrivateEventCreateView, 
    PrivateEventInviteView, 
    PrivateEventDetailView,
    MethodOfPaymentView,
    )


app_name = "events"
urlpatterns = [
    path("", PrivateEventListView.as_view(), name="private_event_list"),
    path("new/", PrivateEventCreateView.as_view(), name="private_event_add"),
    path("<int:pk>/", PrivateEventDetailView.as_view(), name="private_event_detail"),
    path("<int:pk>/invite", PrivateEventInviteView.as_view(), name="invite_private_event"),
    path("payment/", MethodOfPaymentView.as_view(), name="method_of_payment"),
]
