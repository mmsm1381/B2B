from django.contrib.auth.models import update_last_login

from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializers import CustomerSerializer,CreditProviderSerializer,LoginSerializers


class CustomerRegisterApi(CreateAPIView):

    serializer_class = CustomerSerializer



class CreditProviderRegisterApi(CreateAPIView):

    serializer_class = CreditProviderSerializer


class LoginApi(APIView):

    serializer_class = LoginSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})
    