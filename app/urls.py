from django.urls import path
from . import views

urlpatterns = [
    path("", views.FilmList.as_view()),
    path("<pk>", views.FilmDetail.as_view()),
]
