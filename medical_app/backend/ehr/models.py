from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

# class Doctor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) 
#     specialization = models.CharField(max_length=255)
#     contact = models.CharField(max_length=20, default="+0000000000")
#     experience_years = models.IntegerField(default=0)
#     hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE, null=True, blank=True)  

#     def __str__(self):
#         return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialization}"
        
class Doctor(models.Model):
    full_name = models.CharField(max_length=255, default="unkown doc")  
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    contact = models.CharField(max_length=20)
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self):
        return self.full_name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"{self.user.username} - {self.age} years old"
    

class ElectronicHealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    diagnosis = models.TextField()
    prescriptions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.diagnosis[:30]}"
