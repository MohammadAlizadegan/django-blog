from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, max_length=255)
    class Meta:
        model = User
        fields = ('email', 'password', 'password1')

    def validate(self, data):
        if data.get('password') != data.get('password1'):
            raise serializers.ValidationError({'detail': 'Passwords are not match'})
        try:
            validate_password(data.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'email': list(e.messages)})
        return super().validate(data)
    def create(self, validated_data):
        validated_data.pop('password1', None)
        return User.objects.create_user(**validated_data)
