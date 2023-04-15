from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Album, Track
from . import managedb, xmlmusic
from django.apps import apps

# Create your views here.
models = apps.get_app_config('musicutils').get_models()
models = {idx: model for idx, model in enumerate(models)}


def index(request):

    # managedb.insert_data()

    ru_models = {idx: model._meta.verbose_name_plural.title() for idx, model in models.items()}
    content = {
        'models': ru_models
    }
    return render(request, 'musicutils/index.html', content)


def create_xml(request):
    xmlmusic.create_xml(apps.get_app_config('musicutils').get_models())
    return redirect(reverse('music_utils:index'))


def detail(request, table_id):
    model = models[table_id]
    records = model.objects.all().values()
    fields = [f.verbose_name for f in model._meta.fields]

    if model._meta.model_name == 'user':
        for user in User.objects.all():
            user.playlist_size = len(user.userplaylist_set.all())
            user.save()

    for record in records:
        for key, val in record.items():
            if model._meta.model_name == 'track' and key == 'album_id':
                record[key] = Album.objects.get(pk=int(val)).title
            elif model._meta.model_name == 'userplaylist':
                if key == 'user_id':
                    record[key] = User.objects.get(pk=int(val)).__str__
                elif key == 'track_id':
                    record[key] = Track.objects.get(pk=int(val)).title

    content = {
        'records': records,
        'fields': fields,
        'model_name': model._meta.verbose_name_plural.title(),
        'table_id': table_id
    }

    if model._meta.model_name == 'userplaylist':
        users = User.objects.all()
        tracks = Track.objects.all()

        content['users'] = users
        content['tracks'] = tracks

    if model._meta.model_name == 'track':
        albums = Album.objects.all()
        content['albums'] = albums

    return render(request, 'musicutils/detail.html', content)


def add_record(request, table_id):
    model = models[table_id]

    params = [model.objects.order_by('-id').first().id + 1]

    if model._meta.model_name == 'userplaylist':
        params.append(request.POST['user'])
        params.append(request.POST['track'])
    else:
        for key, val in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                params.append(val)

    managedb.add_record(model, params)
    return redirect(reverse('music_utils:detail', args=(table_id,)))


def delete_record(request, table_id, row_id):
    model = models[table_id]
    # print(model.objects.get(pk=row_id))
    managedb.delete_record(model, row_id)
    # record = model.objects().get(pk=row_id)
    # record.delete()
    return redirect(reverse('music_utils:detail', args=(table_id, )))
