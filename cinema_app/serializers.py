from rest_framework import serializers
from .models import Cinema, Room, Movie, MovieSession, Reserve, Ticket, Row, Seat, Discount


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


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    reserve = ReserveSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
