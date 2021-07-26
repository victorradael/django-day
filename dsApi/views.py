from rest_framework import viewsets
from .models import Athlete
from .serializers import AthletsSerializer

class AthletsViewSet(viewsets.ModelViewSet):
    """Show all Athlets"""
    queryset = Athlete.objects.all()
    serializer_class = AthletsSerializer


# Create your views here.
