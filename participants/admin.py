from django.contrib import admin
from .models import Participant

# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("name", "soil_sample_label", "address", "user", 'created')

admin.site.register(Participant, ParticipantAdmin)
