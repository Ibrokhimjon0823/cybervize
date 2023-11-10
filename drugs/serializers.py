from rest_framework import serializers
from drugs.models import Drug, Disease

class DrugDiseaseSearchSerializer(serializers.Serializer):
    query = serializers.CharField()


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class SearchResultSerializer(serializers.Serializer):
    drugs = DrugSerializer(many=True)
    diseases = DiseaseSerializer(many=True)

