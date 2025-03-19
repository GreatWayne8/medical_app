from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    full_name = models.CharField(max_length=255, default="Unknown Doctor")  
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField(default=0)
    contact = models.CharField(max_length=20)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True, related_name="doctors")  

    def __str__(self):
        return self.full_name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_profile")
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True, null=True)  
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name="patients")

    def __str__(self):
        return f"{self.user.username} - {self.age} years old"

class EHR(models.Model):  
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="records")
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name="ehr_records")
    diagnosis = models.TextField()
    prescriptions = models.TextField(blank=True, null=True)  
    treatment_plan = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"EHR: {self.patient.user.username} - {self.diagnosis[:30]}"
