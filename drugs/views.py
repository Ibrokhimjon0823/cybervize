from rest_framework import generics
from .models import Disease, Drug
from .serializers import (
    DiseaseSerializer,
    DrugSerializer,
    DrugDiseaseSearchSerializer,
    SearchResultSerializer,
)


class DiseaseSearchAPIView(generics.ListAPIView):
    serializer_class = DiseaseSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Disease.objects.filter(name__icontains=query)


class DrugSearchAPIView(generics.ListAPIView):
    serializer_class = DrugSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return Drug.objects.filter(name__icontains=query)


class DrugDiseaseSearchAPIView(generics.ListAPIView):
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        diseases = Disease.objects.filter(name__icontains=query)
        drugs = Drug.objects.filter(name__icontains=query)
        return [{'diseases': diseases, 'drugs': drugs}]
