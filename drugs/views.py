from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Drug, Disease
from .serializers import DrugDiseaseSearchSerializer
from django_filters import FilterSet, CharFilter


class DrugDiseaseFilter(FilterSet):
    query = CharFilter(method='filter_query')

    class Meta:
        model = Drug
        fields = []

    def filter_query(self, queryset, name, value):
        return queryset.filter(
            Drug.Q(name__icontains=value) |  # Search drug name
            Disease.Q(diseases__name__icontains=value)  # Search disease name
        ).distinct()


class DrugDiseaseSearchView(generics.ListAPIView):
    serializer_class = DrugDiseaseSearchSerializer
    queryset = Drug.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = DrugDiseaseFilter
