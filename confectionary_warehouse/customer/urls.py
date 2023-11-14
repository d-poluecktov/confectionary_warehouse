from django.urls import path
from .views import CustomerListCreateView, CustomerDetailView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
]
