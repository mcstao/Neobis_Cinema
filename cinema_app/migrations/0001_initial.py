# Generated by Django 4.2.7 on 2023-11-26 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('cinema_name', models.CharField(max_length=100, verbose_name='Кинотеатр')),
                ('cinema_address', models.CharField(max_length=100, verbose_name='Адресс кинотеатра')),
                ('start_work', models.TimeField(verbose_name='Начало работы')),
                ('end_work', models.TimeField(verbose_name='Конец работы')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=250, verbose_name='Название фильма')),
                ('genres', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('duration', models.CharField(max_length=30, verbose_name='Продолжительность')),
                ('poster', models.ImageField(upload_to='', verbose_name='Постер')),
                ('is_active', models.BooleanField(default=True)),
                ('release_day', models.DateField(verbose_name='День релиза')),
                ('end_day', models.DateField(verbose_name='День окончания проката')),
            ],
        ),
        migrations.CreateModel(
            name='MovieSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField(verbose_name='Время показа')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reserved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_type', models.CharField(max_length=100, verbose_name='Тип зала')),
                ('hall_name', models.CharField(max_length=255, verbose_name='Название зала')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_number', models.PositiveIntegerField(verbose_name='Номер ряда')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.room')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.PositiveIntegerField(verbose_name='Номер места')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.room')),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.row')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.movie')),
                ('reserve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.reserve')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.room')),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.row')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.seat')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.moviesession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reserve',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.room'),
        ),
        migrations.AddField(
            model_name='reserve',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.row'),
        ),
        migrations.AddField(
            model_name='reserve',
            name='seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.seat'),
        ),
        migrations.AddField(
            model_name='reserve',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.moviesession'),
        ),
        migrations.AddField(
            model_name='moviesession',
            name='cinema_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.room'),
        ),
        migrations.AddField(
            model_name='moviesession',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema_app.movie'),
        ),
    ]
