from django.urls import path
from .views import DrugDiseaseSearchView

urlpatterns = [
    path('search/', DrugDiseaseSearchView.as_view(), name='drug_disease_search'),
]
