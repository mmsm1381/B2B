from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import SysTransaction

User = get_user_model()

class ConsumerForeignKey(serializers.RelatedField):

    def get_queryset(self):
        return User.objects.filter(is_superuser=False).exclude(id=self.context['request'].user.id)

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
        validated_data["provider"] = self.context["request"].user
        return super().create(validated_data)
    