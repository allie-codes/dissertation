from django.contrib import admin
from .models import Participant

# Register your models here.
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "email",)

admin.site.register(Participant, ParticipantAdmin)
