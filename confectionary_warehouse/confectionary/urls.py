from django.urls import path
from .views import ConfectionaryListCreateView, ConfectionaryDetailView

urlpatterns = [
    path('confectionaries/', ConfectionaryListCreateView.as_view(), name='confectionary-list'),
    path('confectionaries/<uuid:pk>/', ConfectionaryDetailView.as_view(), name='confectionary-detail'),
]
