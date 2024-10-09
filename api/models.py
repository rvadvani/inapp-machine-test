from django.db import models

class Movie(models.Model):
    tconst = models.CharField(max_length=20, primary_key=True)
    title_type = models.CharField(max_length=50)
    primary_title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    is_adult = models.BooleanField(default=False)
    start_year = models.IntegerField(null=True)
    end_year = models.IntegerField(null=True)
    runtime_minutes = models.IntegerField(null=True)
    genres = models.CharField(max_length=255)

    def __str__(self):
        return self.primary_title


class Person(models.Model):
    nconst = models.CharField(max_length=20, primary_key=True)
    primary_name = models.CharField(max_length=255)
    birth_year = models.IntegerField(null=True)
    death_year = models.IntegerField(null=True)
    primary_profession = models.CharField(max_length=255)
    known_for_titles = models.CharField(max_length=255)

    def __str__(self):
        return self.primary_name
