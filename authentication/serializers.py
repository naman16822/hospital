from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentication.models import User

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['profile'] = LoginProfileSerializer(self.user).data
        
        return data
    
class LoginProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password', 'last_login', 'is_active', 'is_superuser', 'is_staff',
            'groups', 'user_permissions', 'date_joined',
        )
        
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'username', 'password', 'password2', 'email', 'first_name', 'last_name',
            'roles', 'address', 'city', 'country', 'origin', 
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'roles': {'required': True},
        }
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password fields did not match.'})
        
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email'),
            roles=validated_data.get('roles', "patient"),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            address=validated_data.get('address'),
            city=validated_data.get('city'),
            country=validated_data.get('country'),
            origin=validated_data.get('origin')
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
