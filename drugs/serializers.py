from rest_framework import serializers


class DrugDiseaseSearchSerializer(serializers.Serializer):
    query = serializers.CharField()
