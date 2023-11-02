from re import fullmatch

from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView

from app.models import Film
from app.serializers import FilmDetailSerializer, FilmSerializer


class FilmList(ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        queryset = Film.objects.all()
        GET = self.request.GET

        if ordering := GET.get('ordering'):
            if not fullmatch(r"-?release_year", ordering):
                message = "Wrong ordering, try (-)release_year"
                raise Http404(message)

            queryset = queryset.order_by(ordering)

        if film_type := GET.get('type'):
            if not film_type.isdigit():
                message = "Wrong type, you should use integer"
                raise Http404(message)

            queryset = queryset.filter(film_type=film_type)

        if category := GET.get('category'):
            if not category.isdigit():
                message = "Wrong category, you should use integer"
                raise Http404(message)

            queryset = queryset.filter(category=category)

        if genre := GET.get('genre'):
            if not genre.isdigit():
                message = "Wrong genre, you should use integer"
                raise Http404(message)

            queryset = queryset.filter(genere__id__contains=genre)

        return queryset


class FilmDetail(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer

