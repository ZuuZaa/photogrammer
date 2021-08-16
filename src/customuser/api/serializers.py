from rest_framework import serializers
from customuser.models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        password2 = serializers.CharField(style = {'input_type': 'password'}, write_only=True)
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def save(self):
        account = CustomUser.create (
        email = self.validated_data['email'],
        first_name = self.validated_data['first_name'],
        last_name = self.validated_data['last_name']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Paswords must match.'})
        account.set_password(password)
        account.save()
        return account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']
