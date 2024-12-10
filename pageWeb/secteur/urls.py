from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProduitViewSet, SecteurViewSet, RepresentativeViewSet, GestionViewSet

router = DefaultRouter()
router.register('produits', ProduitViewSet)
router.register('secteurs', SecteurViewSet)
router.register('representatives', RepresentativeViewSet)
router.register('gestions', GestionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]