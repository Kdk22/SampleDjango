from django.contrib import admin
from .models import Album, Song

admin.site.register(Album) #register this album in admin site or in admin interface
admin.site.register(Song)
