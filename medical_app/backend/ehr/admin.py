from django.contrib import admin
from .models import Hospital, Doctor, Patient, EHR

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Patient)

@admin.register(EHR)
class EHRAdmin(admin.ModelAdmin):
    list_display = ("patient", "doctor", "diagnosis", "created_at")
    search_fields = ("patient__user__username", "doctor__full_name", "diagnosis")
    list_filter = ("created_at",)
