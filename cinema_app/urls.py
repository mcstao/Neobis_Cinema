from django.urls import path
from .views import (CinemaListCreateView, RoomListCreateView,
                    GenreListCreateView, MovieListCreateView,
                    MovieSessionListCreateView, SeatListCreateView,
                    TicketListCreateView)

urlpatterns = [
    path('cinemas/', CinemaListCreateView.as_view(), name='cinema-list-create'),
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movie-sessions/', MovieSessionListCreateView.as_view(), name='movie-session-list-create'),
    path('seats/', SeatListCreateView.as_view(), name='seat-list-create'),
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
]
