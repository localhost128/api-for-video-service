from rest_framework import serializers

from .models import Film, Image


class FilmSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

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

    class Meta:
        model = Film
        fields = '__all__'

