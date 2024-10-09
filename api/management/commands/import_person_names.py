import csv
from api.models import Person
from django.core.management.base import BaseCommand

# python3 manage.py import_person_names

class Command(BaseCommand):
    help = 'Importing person names ...'

    def handle(self, *args, **kwargs):
        
        with open('/home/vikramaditya/Downloads/name.basics.tsv', 'r', encoding='utf-8') as persons_file:
            reader = csv.DictReader(persons_file, delimiter='\t')
            for row in reader:
                person = Person(
                    nconst=row['nconst'],
                    primary_name=row['primaryName'],
                    birth_year=int(row['birthYear']) if row['birthYear'] else None,
                    death_year=int(row['deathYear']) if row['deathYear'] else None,
                    primary_profession=row['primaryProfession'],
                    known_for_titles=row['knownForTitles']
                )
                person.save()
                self.stdout.write(self.style.SUCCESS(f'Imported tconst: {person.nconst} and primary_title: {person.primary_name}'))

        self.stdout.write(self.style.SUCCESS('All the names imported successfully!'))
