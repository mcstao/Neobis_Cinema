from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Cinema(models.Model):
    city = models.CharField(max_length=100, verbose_name='Город')
    cinema_name = models.CharField(max_length=100, verbose_name='Кинотеатр')
    cinema_address = models.CharField(max_length=100, verbose_name='Адресс кинотеатра')
    start_work = models.TimeField(verbose_name='Начало работы')
    end_work = models.TimeField(verbose_name='Конец работы')

    def __str__(self):
        return f"{self.cinema_name} - {self.city} - {self.cinema_address}"


class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall_type = models.CharField(max_length=100)
    hall_name = models.CharField(max_length=255)


def __str__(self):
    return f"{self.cinema} - {self.hall_name}"


class Genre(models.Model):
    genre_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=250, verbose_name='Название фильма')
    genres = models.ManyToManyField(Genre)
    description = models.TextField(max_length=2000, verbose_name='Описание')
    duration = models.CharField(max_length=30, verbose_name='Продолжительность')
    poster = models.ImageField(verbose_name='Постер')
    is_active = models.BooleanField(default=True)
    release_day = models.DateField(verbose_name='День релиза')
    end_day = models.DateField(verbose_name='День окончания проката')

    def __str__(self):
        return self.movie_name


class MovieSession(models.Model):
    show_time = models.DateTimeField(verbose_name='Время показа')
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    cinema_hall = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.movie.movie_name}-{self.show_time}-{self.price}'


class Seat(models.Model):
    room = models.ManyToManyField(Room)
    session = models.ManyToManyField(MovieSession)
    rows = models.PositiveIntegerField(verbose_name='Количество рядов')
    seats_in_row = models.PositiveIntegerField(verbose_name='Количество мест в ряде')
    is_reserved = models.BooleanField(default=False)

    @property
    def seats_quantity(self) -> int:
        return self.rows * self.seats_in_row

    def cancel_time(self):
        current_time = timezone.now()
        time_difference = self.session.show_time - current_time
        return time_difference.total_seconds() <= 1800

    def cancel_reservation(self):
        if self.cancel_time():
            self.is_reserved = False
            self.save()

    def __str__(self):
        return f"{self.room.cinema} - {self.room.hall_name} - Ряд {self.rows}, Место {self.seats_in_row}"


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    session = models.ForeignKey(MovieSession, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.amount}-{self.quantity}'
