from rest_framework import serializers
from .models import Cinema, Room, Genre, Movie, MovieSession, Seat, Ticket


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSessionSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer()
    cinema_hall = RoomSerializer()
    movie = MovieSerializer()

    class Meta:
        model = MovieSession
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Seat
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    cinema = CinemaSerializer()
    room = RoomSerializer()
    movie = MovieSerializer()
    session = MovieSessionSerializer()
    seat = SeatSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'
