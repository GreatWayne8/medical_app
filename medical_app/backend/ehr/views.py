from rest_framework import generics, permissions
from .models import Patient, Doctor, ElectronicHealthRecord
from .serializers import PatientSerializer, DoctorSerializer, EHRSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    return Response({"message": "You have access to this endpoint!"})

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Ensure users can only access their own patient record."""
        return Patient.objects.filter(user=self.request.user)
    
    
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class DoctorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Assign Doctor to Patient
class AssignDoctorView(APIView):
    def post(self, request, patient_id, doctor_id):
        try:
            patient = Patient.objects.get(id=patient_id)
            doctor = Doctor.objects.get(id=doctor_id)
            patient.assigned_doctor = doctor
            patient.save()
            return Response({"message": f"Doctor {doctor.full_name} assigned to patient {patient.full_name}"})
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=404)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=404)

class EHRListCreateView(generics.ListCreateAPIView):
    queryset = ElectronicHealthRecord.objects.all()
    serializer_class = EHRSerializer
    permission_classes = [IsAuthenticated]


