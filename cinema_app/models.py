import decimal

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
    show_time = models.DateTimeField(verbose_name='Время показа', default=timezone.now)
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

    def __str__(self):
        return f"{self.session.movie.movie_name}-{self.session.show_time}-{self.room.hall_name}-Ряд {self.row.row_number}, Место {self.seat.seat_number}"


class Discount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    have_discount = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Ticket(models.Model):
    PAY_METHODS = (
        ('card', 'Картой'),
        ('cash', 'Наличные')

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    session = models.ForeignKey(MovieSession, on_delete=models.CASCADE)
    seat = models.ManyToManyField(Seat)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    pay_method = models.CharField(max_length=20, choices=PAY_METHODS, verbose_name='Метод оплаты')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        self.total_amount = self.session.price * self.quantity
        if self.discount.have_discount:
            self.total_amount *= decimal.Decimal(0.97)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.total_amount}-{self.quantity}'


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.cinema.cinema_name} - {self.created_at}"
