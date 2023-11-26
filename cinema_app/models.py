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
    hall_type = models.CharField(max_length=100, verbose_name='Тип зала')
    hall_name = models.CharField(max_length=255, verbose_name='Название зала')


def __str__(self):
    return f"{self.cinema}-{self.hall_name}-{self.hall_type}"


class Row(models.Model):
    hall = models.ForeignKey(Room, on_delete=models.CASCADE)
    row_number = models.PositiveIntegerField(verbose_name='Номер ряда')

    def __str__(self):
        return f'Ряд {self.row_number}'


class Seat(models.Model):
    hall = models.ForeignKey(Room, on_delete=models.CASCADE)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField(verbose_name='Номер места')

    def __str__(self):
        return f'{self.hall.hall_name}-Ряд{self.row.row_number} Место {self.seat_number}'



class Movie(models.Model):
    movie_name = models.CharField(max_length=250, verbose_name='Название фильма')
    genres = models.CharField(max_length=150)
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


class Reserve(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    session = models.ForeignKey(MovieSession, on_delete=models.CASCADE)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    is_reserved = models.BooleanField(default=False)

    def cancel_time(self):
        current_time = timezone.now()
        time_difference = self.session.show_time - current_time
        return time_difference.total_seconds() <= 1800

    def cancel_reservation(self):
        if self.cancel_time():
            self.is_reserved = False
            self.save()

    def __str__(self):
        return f"{self.session.movie.movie_name}-{self.room.hall_name}-Ряд {self.row.row_number}, Место {self.seat.seat_number}"


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    session = models.ForeignKey(MovieSession, on_delete=models.CASCADE)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.amount}-{self.quantity}'
