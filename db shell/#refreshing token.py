#refreshing token
python manage.py shell

from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()
user = User.objects.get(username="sean")  

refresh = RefreshToken.for_user(user)
access_token = str(refresh.access_token)
refresh_token = str(refresh)

print("New Access Token:", access_token)
print("New Refresh Token:", refresh_token)

from rest_framework_simplejwt.tokens import RefreshToken

refresh = RefreshToken("PASTE_YOUR_REFRESH_TOKEN_HERE") 
new_access_token = str(refresh.access_token)

print("Refreshed Access Token:", new_access_token)


# dr
from django.contrib.auth import get_user_model
from ehr.models import Patient

# Get the user model
User = get_user_model()

# Try fetching the user
try:
    user = User.objects.get(username="johndoe")
except User.DoesNotExist:
    print("User not found. Creating the user now...")
    user = User.objects.create_user(username="johndoe", password="securepassword")

# Check if the user exists
if user:
    existing_patient = Patient.objects.filter(user=user).first()

    if existing_patient:
        print("Patient already exists with ID:", existing_patient.id)
    else:
        new_patient = Patient.objects.create(
            user=user,
            age=30,
            contact="0700000000",
            medical_history="No known conditions"
        )
        print("New Patient ID:", new_patient.id)
