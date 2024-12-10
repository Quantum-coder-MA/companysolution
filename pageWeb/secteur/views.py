from rest_framework import viewsets
from .models import Produit, Secteur, Representative, Gestion
from .serializers import ProduitSerializer, SecteurSerializer, RepresentativeSerializer, GestionSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class SecteurViewSet(viewsets.ModelViewSet):
    queryset = Secteur.objects.all()
    serializer_class = SecteurSerializer

class RepresentativeViewSet(viewsets.ModelViewSet):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer

class GestionViewSet(viewsets.ModelViewSet):
    queryset = Gestion.objects.all()
    serializer_class = GestionSerializer