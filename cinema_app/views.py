from rest_framework import generics
from .models import Cinema, Room, Genre, Movie, MovieSession, Seat, Ticket
from .serializers import (
    CinemaSerializer,
    RoomSerializer,
    GenreSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    SeatSerializer,
    TicketSerializer,
)


class CinemaListCreateView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieSessionListCreateView(generics.ListCreateAPIView):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer


class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
