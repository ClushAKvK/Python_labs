from django.contrib import admin
from .models import *

# Register your models here.


class BasketInline(admin.TabularInline):
    model = Basket
    extra = 1


class ElectronicInline(admin.TabularInline):
    model = Electronic
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [BasketInline]
    list_display = ('first_name', 'last_name')
    ordering = ('id',)


admin.site.register(User, UserAdmin)


class ElectronicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                 {'fields': ['title']}),
        ('Данные об електронике', {'fields': ['manufacturer', 'price']})
    ]
    list_display = ('title', 'manufacturer', 'price')
    inlines = [BasketInline]


admin.site.register(Electronic, ElectronicAdmin)


class BasketAdmin(admin.ModelAdmin):
    list_editable = ('user', 'electronic')
    list_display = ('id', 'user', 'electronic')
    list_filter = ('user', 'electronic')
    ordering = ('id', )


admin.site.register(Basket, BasketAdmin)
