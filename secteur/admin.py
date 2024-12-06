from django.contrib import admin
from .models import Produit, Secteur, Representative, Commercialization, Gestion

admin.site.register(Produit)
admin.site.register(Secteur)
admin.site.register(Representative)
admin.site.register(Commercialization)
admin.site.register(Gestion)
# Register your models here.
