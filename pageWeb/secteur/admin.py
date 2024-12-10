from django.contrib import admin
from .models import (
    GeographicSector, 
    Product, 
    Representative, 
    ProductRepresentativeSector
)

@admin.register(GeographicSector)
class GeographicSectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_sectors')
    search_fields = ('name',)
    
    def display_sectors(self, obj):
        return ", ".join([sector.name for sector in obj.sectors.all()])
    display_sectors.short_description = "Sectors"

@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'display_sectors')
    search_fields = ('name', 'email')
    
    def display_sectors(self, obj):
        return ", ".join([sector.name for sector in obj.sectors.all()])
    display_sectors.short_description = "Managed Sectors"

@admin.register(ProductRepresentativeSector)
class ProductRepresentativeSectorAdmin(admin.ModelAdmin):
    list_display = ('product', 'representative', 'sector')
    list_filter = ('product', 'representative', 'sector')