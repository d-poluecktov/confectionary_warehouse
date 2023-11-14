from django.urls import path
from .views import (
    CountryListCreateView, CountryDetailView,
    CityListCreateView, CityDetailView,
    ManufacturerListCreateView, ManufacturerDetailView,
)

urlpatterns = [

    path('countries/', CountryListCreateView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country-detail'),


    path('cities/', CityListCreateView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='city-detail'),


    path('manufacturers/', ManufacturerListCreateView.as_view(), name='manufacturer-list'),
    path('manufacturers/<int:pk>/', ManufacturerDetailView.as_view(), name='manufacturer-detail'),
]
