from rest_framework import serializers
from .models import Patient, Doctor, ElectronicHealthRecord

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class EHRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicHealthRecord
        fields = '__all__'
