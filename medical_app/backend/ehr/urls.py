from django.urls import path
from .views import PatientListCreateView, DoctorListCreateView, EHRListCreateView,protected_endpoint

urlpatterns = [
    path("patients/", PatientListCreateView.as_view(), name="patients"),
    path("doctors/", DoctorListCreateView.as_view(), name="doctors"),
    path("", EHRListCreateView.as_view(), name="ehr"),
    path("protected-endpoint/", protected_endpoint, name="protected-endpoint"),

]
