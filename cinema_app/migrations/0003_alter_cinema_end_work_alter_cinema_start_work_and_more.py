# Generated by Django 4.2.7 on 2023-11-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0002_genre_movie_moviesession_room_seat_ticket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='end_work',
            field=models.TimeField(verbose_name='Конец работы'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='start_work',
            field=models.TimeField(verbose_name='Начало работы'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=30, verbose_name='Продолжительность'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='end_day',
            field=models.DateField(verbose_name='День окончания проката'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_name',
            field=models.CharField(max_length=250, verbose_name='Название фильма'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_day',
            field=models.DateField(verbose_name='День релиза'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='show_time',
            field=models.DateTimeField(verbose_name='Время показа'),
        ),
    ]