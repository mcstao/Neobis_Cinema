from rest_framework import serializers
from .models import Cinema, Room, Movie, MovieSession, Reserve, Ticket, Row, Seat, Discount, Feedback, PurchaseHistory


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
        fields = ['user', 'have_discount']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['user', 'cinema', 'room', 'movie', 'session', 'seat', 'pay_method', 'quantity', 'discount',
                  'total_amount']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class PurchaseHistorySerializer(serializers.ModelSerializer):
    movies_info = MovieSessionSerializer(many=True, read_only=True)
    ticket_info
    class Meta:
        model = PurchaseHistory
        fields = '__all__'

