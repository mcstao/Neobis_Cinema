from django.contrib import admin

from cinema_app.models import Cinema, Room, Genre, MovieSession, Movie, Seat, Ticket

admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieSession)
admin.site.register(Seat)
admin.site.register(Ticket)