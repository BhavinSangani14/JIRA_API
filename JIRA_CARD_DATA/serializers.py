from rest_framework import serializers
from .models import CredsModel, CardDataModel


class CredsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CredsModel
        fields = "__all__"


class CardDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardDataModel
        fields = "__all__"   

