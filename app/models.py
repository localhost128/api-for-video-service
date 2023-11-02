from django.db import models
from django.core.validators import MinValueValidator


class Type(models.Model):
    name = models.CharField(unique=True, max_length=50)


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=50)


class Audio(models.Model):
    name = models.CharField(unique=True, max_length=50)


class Category(models.Model):
    name = models.CharField(unique=True, max_length=3)


class Image(models.Model):
    url = models.URLField()
    is_main = models.BooleanField(default=True)


class Film(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, max_length=350)
    release_year = models.IntegerField(validators=[MinValueValidator(1900)])
    film_type = models.ForeignKey("Type", on_delete=models.PROTECT)
    genere = models.ManyToManyField("Genre", blank=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

