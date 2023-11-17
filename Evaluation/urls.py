# urls.py

from django.urls import path
from .views import GetClientEvaluations,AddEvaluations

urlpatterns = [
    path('client-evaluations/', GetClientEvaluations.as_view(), name='client-evaluations'),
    path('create-evaluations/', AddEvaluations.as_view(), name='create_evaluation'),

    # Add other URLs as needed
]
