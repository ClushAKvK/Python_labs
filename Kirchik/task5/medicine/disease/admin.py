from django.contrib import admin
from .models import *

# Register your models here.


class DiseaseSymptomInline(admin.TabularInline):
    model = DiseaseSymptom
    extra = 1


class SymptomInline(admin.TabularInline):
    model = Symptom
    extra = 1


class DiseaseAdmin(admin.ModelAdmin):
    inlines = [DiseaseSymptomInline]
    list_display = ('name', 'chance_to_survive', 'description')
    ordering = ('id',)


admin.site.register(Disease, DiseaseAdmin)


class SymptomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                 {'fields': ['name']}),
        ('Данные о симптомах', {'fields': ['description']})
    ]
    list_display = ('name', 'description')
    inlines = [DiseaseSymptomInline]


admin.site.register(Symptom, SymptomAdmin)

#
# class TrackAdmin(admin.ModelAdmin):
#
#     def time_seconds(self, obj):
#         return obj.duration.strftime("%H:%M:%S")
#
#     fieldsets = [
#         (None, {'fields': ['title']}),
#         ('Данные о треке', {'fields': ['singer', 'duration', 'album']})
#     ]
#
#     time_seconds.admin_order_field = 'duration'
#     time_seconds.short_description = 'Продолжительность'
#
#     list_display = ('title', 'singer', 'time_seconds')
#     list_filter = ('singer',)
#     inlines = [UserPlaylistInline]
#
#
# admin.site.register(Track, TrackAdmin)


class DiseaseSymptomAdmin(admin.ModelAdmin):
    list_editable = ('disease', 'symptom')
    list_display = ('id', 'disease', 'symptom')
    list_filter = ('disease', 'symptom')
    ordering = ('id', )


admin.site.register(DiseaseSymptom, DiseaseSymptomAdmin)
