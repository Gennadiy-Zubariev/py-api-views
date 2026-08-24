from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorDetail,
    ActorList,
    MovieViewSet,
    CinemaHallViewSet,
)

cinema_hall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

router = routers.DefaultRouter()

router.register("movies", MovieViewSet, basename="movie")

urlpatterns = [
    path("api/cinema/genres/", GenreList.as_view(), name="genre-list"),
    path("api/cinema/genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("api/cinema/actors/", ActorList.as_view(), name="actor-list"),
    path("api/cinema/actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("api/cinema/cinema_halls/", cinema_hall_list, name="cinema-hall-list"),
    path("api/cinema/cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"),
    path("api/cinema/", include(router.urls)),
]

app_name = "cinema"
