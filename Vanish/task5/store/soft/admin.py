from django.contrib import admin
from .models import *

# Register your models here.


class SoftwareCompanyInline(admin.TabularInline):
    model = SoftwareCompany
    extra = 1


class CompanyInline(admin.TabularInline):
    model = Company
    extra = 1


class SoftwareAdmin(admin.ModelAdmin):
    inlines = [SoftwareCompanyInline]
    list_display = ('name', 'slogan')
    ordering = ('id',)


admin.site.register(Software, SoftwareAdmin)


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                 {'fields': ['name']}),
        ('Данные о компании',  {'fields': ['description']})
    ]
    list_display = ('name', 'description')
    inlines = [SoftwareCompanyInline]


admin.site.register(Company, CompanyAdmin)


class SoftwareCompanyAdmin(admin.ModelAdmin):
    list_editable = ('software', 'company')
    list_display = ('id', 'software', 'company')
    list_filter = ('software', 'company')
    ordering = ('id', )


admin.site.register(SoftwareCompany, SoftwareCompanyAdmin)
