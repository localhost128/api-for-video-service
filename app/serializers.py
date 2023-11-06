from rest_framework import serializers

from .models import Film, Image


class FilmSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    film_type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')



    def get_img(self, film):
        qs = Image.objects.filter(is_main=True, film=film)
        if qs:
            return qs[0].url
        return "No main image"

    class Meta:
        model = Film
        fields = '__all__'


class FilmDetailSerializer(serializers.ModelSerializer):
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )
    film_type = serializers.SlugRelatedField(read_only=True, slug_field='name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Film
        fields = '__all__'

