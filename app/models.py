from django.db import models
from django.core.validators import MinValueValidator


class Type(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def  __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def  __str__(self):
        return self.name


class Audio(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def  __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(unique=True, max_length=3)

    def  __str__(self):
        return self.name


class Image(models.Model):
    url = models.URLField()
    is_main = models.BooleanField(default=True)
    film = models.ForeignKey(
            "Film", related_name="images", on_delete=models.CASCADE)

    def  __str__(self):
        return self.url


class Film(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, max_length=350)
    release_year = models.IntegerField(validators=[MinValueValidator(1900)])
    film_type = models.ForeignKey("Type", on_delete=models.PROTECT)
    genres = models.ManyToManyField("Genre", blank=True)
    category = models.ForeignKey("Category", on_delete=models.PROTECT)

    get_latest_by = ["name", "-release_year"]

    def  __str__(self):
        return self.name

