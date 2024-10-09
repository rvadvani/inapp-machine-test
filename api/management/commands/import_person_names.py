import csv
from api.sqlalchemy_config import session
from api.models import Person
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Importing person names ...'

    def handle(self, *args, **kwargs):
        with open('/home/vikramaditya/Downloads/name.basics.tsv', 'r', encoding='utf-8') as persons_file:
            reader = csv.DictReader(persons_file, delimiter='\t')
            for row in reader:
    
                person = Person(
                    nconst=row['nconst'],
                    primary_name=row['primaryName'],
                    birth_year=int(row['birthYear']) if row['birthYear'] and row['birthYear'] != '\\N' else None,
                    death_year=int(row['deathYear']) if row['deathYear'] and row['deathYear'] != '\\N' else None,
                    primary_profession=row['primaryProfession'],
                    known_for_titles=row['knownForTitles']
                )

    
                session.add(person)

    
                self.stdout.write(self.style.SUCCESS(f'Prepared to import nconst: {person.nconst} and primary_name: {person.primary_name}'))


            session.commit()

        self.stdout.write(self.style.SUCCESS('All the names imported successfully!'))
