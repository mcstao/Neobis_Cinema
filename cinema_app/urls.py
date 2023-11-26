from django.urls import path
from .views import *

urlpatterns = [
    path('cinemas/', CinemaListView.as_view(), name='cinema-list'),
    path('cinemas/create/', CinemaCreateView.as_view(), name='cinema-create'),
    path('cinemas/update/<int:pk>/', CinemaUpdateView.as_view(), name='cinema-update'),
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('movie-sessions/', MovieSessionListView.as_view(), name='movie-session-list'),
    path('movie-sessions/create/', MovieSessionCreateView.as_view(), name='movie-session-create'),
    path('movie-sessions/update/<int:pk>/', MovieUpdateView.as_view(), name='movie-session-update'),
    path('rows/', RowListCreateView.as_view(), name='rows-list-create'),
    path('seats/', SeatListCreateView.as_view(), name='seats-list-create'),
    path('reserve/', ReserveListCreateView.as_view(), name='reserve-list-create'),
    path('discount/', DiscountListCreateView.as_view()),
    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
]
