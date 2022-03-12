from rest_framework import serializers

from .models import SysTransaction


class SysTransactionSerializer(serializers.ModelSerializer):


    class Meta: 
        model = SysTransaction
        fields = ("consumer","amount","provider",)
        read_only_fields = ['provider']


    def create(self, validated_data):
        validated_data["provider"] = self.context["request"].user
        return super().create(validated_data)
    