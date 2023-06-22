from django.urls import path
from common import views

urlpatterns = [
    path("", views.Invitation.as_view(), name='invitation'),
]