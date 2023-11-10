from django.urls import path
from .views import DiseaseSearchAPIView, DrugSearchAPIView, DrugDiseaseSearchAPIView

urlpatterns = [
    path('api/diseases/', DiseaseSearchAPIView.as_view(), name='disease-search'),
    path('api/drugs/', DrugSearchAPIView.as_view(), name='drug-search'),
    path('api/drug-disease-search/', DrugDiseaseSearchAPIView.as_view(), name='drug-disease-search'),
]
