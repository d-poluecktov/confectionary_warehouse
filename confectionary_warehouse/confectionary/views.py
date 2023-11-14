from rest_framework import generics
from .models import Confectionary
from .serializers import ConfectionarySerializer


class ConfectionaryListCreateView(generics.ListCreateAPIView):
    queryset = Confectionary.objects.all()
    serializer_class = ConfectionarySerializer


class ConfectionaryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Confectionary.objects.all()
    serializer_class = ConfectionarySerializer
