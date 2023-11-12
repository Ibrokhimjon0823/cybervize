import json
import sys
import os
import django
import pathlib

from drugs.models import Drug, Disease


def load_data():
    pass

    path = pathlib.Path(__file__).parent.resolve()

    sys.path.append(str(path.parent))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

    django.setup()

    json_file = path/'dataset.json'

    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        drugs_data = data.get('drugs', [])

        for drug_data in drugs_data:
            diseases_data = drug_data.get('diseases', [])
            diseases = [Disease.objects.get_or_create(name=disease)[0] for disease in diseases_data]
            drug = Drug(
                id=drug_data['id'],
                description=drug_data['description'],
                name=drug_data['name'],
                released=drug_data['released']
            )
            drug.save()

            drug.diseases.add(*diseases)

        print(f"Successfully loaded {len(drugs_data)} drugs into the database.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    load_data()