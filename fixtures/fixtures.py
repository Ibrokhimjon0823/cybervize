import json
import sys
import os
import django
import pathlib


path = pathlib.Path(__file__).parent.resolve()


sys.path.append(str(path.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# Initialize Django ORM
django.setup()

from drugs.models import Drug, Disease

# Load JSON data from the file
json_file = path/'dataset.json'

try:
    with open(json_file, 'r') as file:
        data = json.load(file)

    drugs_data = data.get('drugs', [])  # Extract 'drugs' data from the JSON

    for drug_data in drugs_data:
        # Extract 'diseases' data and create Disease instances
        diseases_data = drug_data.get('diseases', [])
        diseases = [Disease.objects.get_or_create(name=disease)[0] for disease in diseases_data]

        # Create and save the Drug instance
        drug = Drug(
            id=drug_data['id'],
            description=drug_data['description'],
            name=drug_data['name'],
            released=drug_data['released']
        )
        drug.save()

        # Add the related diseases to the drug
        drug.diseases.add(*diseases)

    print(f"Successfully loaded {len(drugs_data)} drugs into the database.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
