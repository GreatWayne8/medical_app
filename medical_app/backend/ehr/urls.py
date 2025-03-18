from django.urls import path
from .views import PatientListCreateView, DoctorListCreateView, EHRListCreateView,protected_endpoint,PatientRetrieveUpdateDestroyView,DoctorRetrieveUpdateDestroyView,AssignDoctorView

urlpatterns = [
    path("patients/", PatientListCreateView.as_view(), name="patients"),
    path("doctors/", DoctorListCreateView.as_view(), name="doctors"),
    path("", EHRListCreateView.as_view(), name="ehr"),
    path("protected-endpoint/", protected_endpoint, name="protected-endpoint"),
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),
    path('assign-doctor/<int:patient_id>/<int:doctor_id>/', AssignDoctorView.as_view(), name='assign-doctor'),


]
