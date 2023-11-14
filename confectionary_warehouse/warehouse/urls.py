from django.urls import path
from .views import WarehouseListCreateView, WarehouseDetailView, EmployeeListCreateView, EmployeeDetailView

urlpatterns = [

    path('warehouses/', WarehouseListCreateView.as_view(), name='warehouse-list'),
    path('warehouses/<int:pk>/', WarehouseDetailView.as_view(), name='warehouse-detail'),

    path('employees/', EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]
