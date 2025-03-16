from django.urls import path
from .views import PatientListCreateView, DoctorListCreateView, EHRListCreateView

urlpatterns = [
    path("patients/", PatientListCreateView.as_view(), name="patients"),
    path("doctors/", DoctorListCreateView.as_view(), name="doctors"),
    path("ehr/", EHRListCreateView.as_view(), name="ehr"),
]
