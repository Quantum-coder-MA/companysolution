# urls.py
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from secteur.views import dashboard_view  
from rest_framework.routers import DefaultRouter
from .views import (
    ProduitViewSet, SecteurViewSet, RepresentativeViewSet, 
    CommercializationViewSet, GestionViewSet
)

router = DefaultRouter()
router.register(r'produits', ProduitViewSet)
router.register(r'secteurs', SecteurViewSet)
router.register(r'representatives', RepresentativeViewSet)
router.register(r'commercializations', CommercializationViewSet)
router.register(r'gestions', GestionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', dashboard_view, name='dashboard'), 
]