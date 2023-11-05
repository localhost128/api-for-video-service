import csv
from random import choice, randint
from pathlib import Path

from django.db import migrations
from django.conf import settings

def fill_model(apps, model_name):
    Model = apps.get_model('app', model_name)
    path_to_file = Path(settings.BASE_DIR) / f"app/db_filling/{model_name}.csv"

    with open(path_to_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Model(name=row["name"]).save()



def fill_characteristics(apps, schema_editor):
    fill_model(apps, 'Type')
    fill_model(apps, 'Category')
    fill_model(apps, 'Genre')
    fill_model(apps, 'Audio')
 

def fill_films(apps, schema_editor):
    Film = apps.get_model('app', 'Film')
    categories = apps.get_model('app', 'Category').objects.all()
    types = apps.get_model('app', 'Type').objects.all()
    genres = apps.get_model('app', 'Genre').objects.all()

    path_to_file = Path(settings.BASE_DIR) / f"app/db_filling/Film.csv"


    with open(path_to_file, newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            film = Film(
                    name=row['name'],
                    description=row['description'],
                    release_year=int(row['release_year']),
                    film_type=choice(types),
                    category=choice(categories),
                    )
            film.save()

            for _ in range(randint(0, 3)):
                film.genres.add(choice(genres))

            film.images.create(url="https://image-url-main.com", is_main=True)
            film.images.create(url="https://image-url.com", is_main=False)

    
class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_characteristics),
        migrations.RunPython(fill_films),
    ]
