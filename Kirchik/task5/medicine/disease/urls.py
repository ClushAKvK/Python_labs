from django.contrib import admin
from django.urls import path
from . import views

app_name = 'disease'
urlpatterns = [
    path('', views.index, name='index'),
    path('/create_xml', views.create_xml, name='create_xml'),
    path('<int:table_id>/detail', views.detail, name='detail'),
    path('<int:table_id>/add_record', views.add_record, name='add_record'),
    path('<int:table_id>/<int:row_id>/delete_record', views.delete_record, name='delete_record')
]
