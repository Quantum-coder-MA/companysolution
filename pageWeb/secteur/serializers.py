from rest_framework import serializers
from .models import Produit, Secteur, Representative, Gestion

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class SecteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secteur
        fields = '__all__'

class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        fields = '__all__'

class GestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestion
        fields='__all__'