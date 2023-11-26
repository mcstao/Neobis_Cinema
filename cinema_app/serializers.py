from rest_framework import serializers
from .models import Cinema, Room, Movie, MovieSession, Reserve, Ticket, Row, Seat


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

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


class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class ReserveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserve
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    cinema = CinemaSerializer()
    room = RoomSerializer()
    movie = MovieSerializer()
    session = MovieSessionSerializer()
    row = RowSerializer()
    seat = SeatSerializer()
    reserve = ReserveSerializer()


    class Meta:
        model = Ticket
        fields = '__all__'
