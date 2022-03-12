from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import CreditProvider,Customer


class CustomerSerializer(serializers.ModelSerializer):


    class Meta :
        model = Customer
        fields = ('email','password','phone_number')
        write_only_fields = ('password',)


class CreditProviderSerializer(serializers.ModelSerializer):


    class Meta :
        model = CreditProvider
        fields = ('email','password','business_name')
        write_only_fields = ('password',)

    def create(self, validated_data):
        validated_data['is_staff'] = True
        return super().create(validated_data)



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