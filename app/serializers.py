from rest_framework import serializers

from .models import Film, Image


class FilmDetailSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='url')

    film_type = serializers.SlugRelatedField(
        read_only=True, slug_field='name')

    category = serializers.SlugRelatedField(
        read_only=True, slug_field='name')

    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')

    class Meta:
        model = Film
        fields = ['id', 'name', 'description', 'release_year',
                  'film_type', 'genre', 'category', 'images']


class FilmSerializer(FilmDetailSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, film):
        qs = Image.objects.filter(is_main=True, film=film)
        if qs:
            return qs[0].url
        return "No main image"

