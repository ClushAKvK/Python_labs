from django.contrib import admin
from .models import *

# Register your models here.


class UserPlaylistInline(admin.TabularInline):
    model = UserPlaylist
    extra = 1


class TrackInline(admin.TabularInline):
    model = Track
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [UserPlaylistInline]
    list_display = ('last_name', 'first_name', 'playlist_size')
    ordering = ('id',)


admin.site.register(User, UserAdmin)


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Данные об альбоме', {'fields': ['description', 'pab_date']})
    ]
    list_display = ('title', 'pab_date')
    inlines = [TrackInline]


admin.site.register(Album, AlbumAdmin)


class TrackAdmin(admin.ModelAdmin):

    def time_seconds(self, obj):
        return obj.duration.strftime("%H:%M:%S")

    fieldsets = [
        (None, {'fields': ['title']}),
        ('Данные о треке', {'fields': ['singer', 'duration', 'album']})
    ]

    time_seconds.admin_order_field = 'duration'
    time_seconds.short_description = 'Продолжительность'

    list_display = ('title', 'singer', 'time_seconds')
    list_filter = ('singer',)
    inlines = [UserPlaylistInline]


admin.site.register(Track, TrackAdmin)


class UserPlaylistAdmin(admin.ModelAdmin):
    list_editable = ('user', 'track')
    list_display = ('id', 'user', 'track')
    list_filter = ('user', 'track')
    ordering = ('id', )


admin.site.register(UserPlaylist, UserPlaylistAdmin)
