from django.contrib import admin
from .models import Meetup , Location , Joiners


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title','slug','location')
    list_filter = ( 'location' ,)
    prepopulated_fields = {'slug' : ('title' ,)}


# Register your models here.
admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Joiners)

#python3 manage.py migrate