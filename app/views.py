from re import fullmatch

from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import exception_handler

from app.models import Film
from app.serializers import FilmDetailSerializer, FilmSerializer


class FilmList(ListAPIView):
    serializer_class = FilmSerializer

    def get_queryset(self):
        self.serializer_class.Meta.fields = '__all__'

        queryset = Film.objects.all()
        GET = self.request.GET

        if ordering := GET.get('ordering'):
            print(ordering)
            if not fullmatch(r"-?release_year", ordering):
                raise Http404
            queryset = queryset.order_by(ordering)

        film_type = GET.get('type')
        category = GET.get('category')
        genre = GET.get('genre')

        filters = (film_type, category, genre)

        if any(filters):
            if not (all(filters) and all(map(lambda x: x.isdigit(), filters))):
                raise Http404
            queryset = queryset.filter(
                    film_type=film_type,
                    category=category,
                    generes__id__contains=genre
                    )
            self.serializer_class.Meta.fields = [
                    "id", "name", "release_year", "img"
                    ]

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

