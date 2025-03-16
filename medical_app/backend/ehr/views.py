from rest_framework import generics
from .models import Patient, Doctor, ElectronicHealthRecord
from .serializers import PatientSerializer, DoctorSerializer, EHRSerializer
from rest_framework.permissions import IsAuthenticated

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class EHRListCreateView(generics.ListCreateAPIView):
    queryset = ElectronicHealthRecord.objects.all()
    serializer_class = EHRSerializer
    permission_classes = [IsAuthenticated]
