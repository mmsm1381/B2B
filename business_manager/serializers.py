from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import SysTransaction,Wallet

User = get_user_model()

class ConsumerForeignKey(serializers.RelatedField):

    def get_queryset(self):
        return Wallet.objects.exclude(owner=self.context['request'].user)

    def to_representation(self, value):
        return str(value)

class SysTransactionSerializer(serializers.ModelSerializer):

    consumer = ConsumerForeignKey()
    provider = serializers.StringRelatedField()

    class Meta: 
        model = SysTransaction
        fields = ("provider","amount","consumer",'status',)
        read_only_fields = ['provider',"status",]


    def create(self, validated_data):
        validated_data["provider"] = self.context["request"].user.wallet
        return super().create(validated_data)
    