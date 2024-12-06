# serializers.py
from rest_framework import serializers
from .models import Produit, Secteur, Representative, Commercialization, Gestion

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ['id', 'nom', 'label', 'price']

class SecteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secteur
        fields = ['id', 'nom', 'ville', 'region']

class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        fields = ['id', 'nom', 'prenom', 'email', 'adress', 'telephone']

class CommercializationSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    secteur = SecteurSerializer(read_only=True)

    class Meta:
        model = Commercialization
        fields = ['id', 'produit', 'secteur']

class GestionSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    secteur = SecteurSerializer(read_only=True)
    representative = RepresentativeSerializer(read_only=True)

    class Meta:
        model = Gestion
        fields = ['id', 'produit', 'secteur', 'representative', 'label', 'price']