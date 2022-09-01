from django.contrib import admin
from .models import Result

# Register your models here.
class ResultAdmin(admin.ModelAdmin):
    list_display = ("soil_sample_label", "sample_number")

admin.site.register(Result, ResultAdmin)