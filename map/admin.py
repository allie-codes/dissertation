from django.contrib import admin
from .models import MapCoordinate

# Register your models here.
class MapCoordinateAdmin(admin.ModelAdmin):
    list_display = ("participant", "address", "latitude", "longitude",)

admin.site.register(MapCoordinate, MapCoordinateAdmin)