import json
from django.urls import reverse
from rest_framework import status
import pytest

# Import your Django app models and views
from .models import Disease, Drug
from .views import DiseaseSearchAPIView, DrugSearchAPIView, DrugDiseaseSearchAPIView


@pytest.mark.django_db
class TestDiseaseSearchAPIView:
    @pytest.fixture
    def disease(self):
        return Disease.objects.create(name="Rak")

    def test_disease_search(self, rf, disease):
        url = reverse('disease-search')
        request = rf.get(url, {'query': 'Rak'})
        response = DiseaseSearchAPIView.as_view()(request)
        assert response.status_code == status.HTTP_200_OK
        assert disease.name in response.data[0]['name']


@pytest.mark.django_db
class TestDrugSearchAPIView:
    @pytest.fixture
    def drug(self):
        return Drug.objects.create(name="Qupen")

    def test_drug_search(self, rf, drug):
        url = reverse('drug-search')
        request = rf.get(url, {'query': 'Qupen'})
        response = DrugSearchAPIView.as_view()(request)
        assert response.status_code == status.HTTP_200_OK
        assert drug.name in response.data[0]['name']

@pytest.mark.django_db
class TestDrugDiseaseSearchAPIView:
    @pytest.fixture
    def disease_and_drug(self):
        disease = Disease.objects.create(name="Rak")
        drug = Drug.objects.create(name="Qupen")
        disease.drugs.add(drug)
        return disease, drug

    def test_drug_disease_search(self, rf, disease_and_drug):
        url = reverse('drug-disease-search')
        request = rf.get(url, {'query': 'Rak'})
        response = DrugDiseaseSearchAPIView.as_view()(request)
        assert response.status_code == status.HTTP_200_OK
        assert disease_and_drug[0].name in response.data[0]['diseases'][0]['name']
        assert disease_and_drug[1].name in response.data[0]['drugs'][0]['name']
