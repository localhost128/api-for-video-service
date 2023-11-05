from re import fullmatch

from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import exception_handler

from app.models import Film
from app.serializers import FilmDetailSerializer, FilmSerializer


class FilmList(ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        queryset = Film.objects.all()
        GET = self.request.GET

        if ordering := GET.get('ordering'):
            if not fullmatch(r"-?release_year", ordering):
                raise Http404
            queryset = queryset.order_by(ordering)

        if film_type := GET.get('type'):
            if not film_type.isdigit():
                raise Http404
            queryset = queryset.filter(film_type=film_type)

        if category := GET.get('category'):
            if not category.isdigit():
                raise Http404
            queryset = queryset.filter(category=category)

        if genre := GET.get('genre'):
            if not genre.isdigit():
                raise Http404
            queryset = queryset.filter(genere__id__contains=genre)

        if not (search := GET.get('search')) is None:
            if not search:
                raise Http404
            queryset = queryset.filter(name__contains=search)

        return queryset


class FilmDetail(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer


def castom_exeption_hendler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        match response.status_code:
            case 404:
                response.data['detail'] = "не коректный запрос," \
                        "неправильные параметры фильтрации / сортировки," \
                        "неправильная страница"
            case 500:
                response.data['deatil'] = "ошибка сервера"
            case _:
                response.data['status_code'] = response.status_code

    return response

