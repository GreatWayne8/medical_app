from rest_framework import serializers
from .models import Patient, Doctor, EHR

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    assigned_doctor = DoctorSerializer(read_only=True)
    class Meta:
        model = Patient
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}} 

class EHRSerializer(serializers.ModelSerializer):
    class Meta:
        model = EHR
        fields = '__all__'
