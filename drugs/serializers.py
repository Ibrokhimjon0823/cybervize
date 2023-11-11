from rest_framework import serializers
from drugs.models import Drug, Disease

class DrugDiseaseSearchSerializer(serializers.Serializer):
    query = serializers.CharField()


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('id', 'name')


class DrugSerializer(serializers.ModelSerializer):
    formatted_release_date = serializers.SerializerMethodField()
    diseases = DiseaseSerializer(many=True, read_only=True)
    class Meta:
        model = Drug
        fields = ('id', 'diseases', 'description', 'name', 'formatted_release_date')

    def get_formatted_release_date(self, obj):
        return obj.formatted_release_date()


class SearchResultSerializer(serializers.Serializer):
    drugs = DrugSerializer(many=True)
    diseases = DiseaseSerializer(many=True, read_only=True)

