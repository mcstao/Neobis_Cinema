from django.contrib import admin

from cinema_app.models import Cinema, Room, MovieSession, Movie, Reserve, Ticket, Seat, Row

admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Row)
admin.site.register(Seat)
admin.site.register(Movie)
admin.site.register(MovieSession)
admin.site.register(Reserve)
admin.site.register(Ticket)
