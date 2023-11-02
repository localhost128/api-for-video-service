from re import fullmatch

from rest_framework.generics import ListAPIView, RetrieveAPIView
from app.models import Film
from app.serializers import FilmDetailSerializer, FilmSerializer


class FilmList(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_queryset(self):
        ordering = self.request.GET.get('ordering')

        if fullmatch(r"-?release_year", ordering):
            self.queryset = self.queryset.order_by(ordering)

        return self.queryset


class FilmDetail(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer

