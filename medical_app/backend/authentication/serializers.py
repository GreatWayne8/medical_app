from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get("email")
#         password = data.get("password")

#         if email and password:
#             user = authenticate(username=email, password=password)  # 🔹 Authenticate user
#             if not user:
#                 raise serializers.ValidationError("Invalid email or password")
#             data["user"] = user  # Attach user object
#         else:
#             raise serializers.ValidationError("Both email and password are required")
        
#         return data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")

        if not email and not username:
            raise serializers.ValidationError("A username or email is required.")

        user = None
        if email:
            user = User.objects.filter(email=email).first()
        elif username:
            user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            return user
        raise serializers.ValidationError("Invalid credentials.")


