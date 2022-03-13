from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):


    class Meta :
        model = User
        fields = ('user_name','password','is_staff')
        write_only_fields = ('password',)


class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    def validate(self, data):
        username = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = ('Unable to log in with provided informations.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data