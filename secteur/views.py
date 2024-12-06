# views.py
from rest_framework import viewsets
from .models import Produit, Secteur, Representative, Commercialization, Gestion
from .serializers import (
    ProduitSerializer, SecteurSerializer, RepresentativeSerializer, 
    CommercializationSerializer, GestionSerializer
)

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class SecteurViewSet(viewsets.ModelViewSet):
    queryset = Secteur.objects.all()
    serializer_class = SecteurSerializer

class RepresentativeViewSet(viewsets.ModelViewSet):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer

class CommercializationViewSet(viewsets.ModelViewSet):
    queryset = Commercialization.objects.all()
    serializer_class = CommercializationSerializer

class GestionViewSet(viewsets.ModelViewSet):
    queryset = Gestion.objects.all()
    serializer_class = GestionSerializer
    


from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'index.html')