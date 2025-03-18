from rest_framework import serializers
from .models import Patient, Doctor, ElectronicHealthRecord

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}} 

class EHRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicHealthRecord
        fields = '__all__'
