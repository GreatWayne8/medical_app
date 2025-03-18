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
