from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Electronic, Basket
from . import managedb, xml_technic
from django.apps import apps

# Create your views here.
models = apps.get_app_config('technic').get_models()
models = {idx: model for idx, model in enumerate(models)}


def index(request):

    # managedb.insert_data()

    ru_models = {idx: model._meta.verbose_name_plural.title() for idx, model in models.items()}
    content = {
        'models': ru_models
    }
    return render(request, 'technic/index.html', content)


def create_xml(request):
    xml_technic.create_xml(apps.get_app_config('technic').get_models())
    return redirect(reverse('technic:index'))


def detail(request, table_id):
    model = models[table_id]
    records = model.objects.all().values()
    fields = [f.verbose_name for f in model._meta.fields]

    for record in records:
        for key, val in record.items():
            if model._meta.model_name == 'basket':
                if key == 'user_id':
                    record[key] = User.objects.get(pk=int(val)).__str__
                elif key == 'electronic_id':
                    record[key] = Electronic.objects.get(pk=int(val)).__str__

    content = {
        'records': records,
        'fields': fields,
        'model_name': model._meta.verbose_name_plural.title(),
        'table_id': table_id
    }

    if model._meta.model_name == 'basket':
        users = User.objects.all()
        electronics = Electronic.objects.all()

        content['users'] = users
        content['electronics'] = electronics

    return render(request, 'technic/detail.html', content)


def add_record(request, table_id):
    model = models[table_id]

    try:
        params = [model.objects.order_by('-id').first().id + 1]
    except AttributeError:
        params = [1]

    if model._meta.model_name == 'basket':
        params.append(request.POST['user'])
        params.append(request.POST['electronic'])
    else:
        for key, val in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                params.append(val)

    managedb.add_record(model, params)
    return redirect(reverse('technic:detail', args=(table_id,)))


def delete_record(request, table_id, row_id):
    model = models[table_id]
    # print(model.objects.get(pk=row_id))
    managedb.delete_record(model, row_id)
    # record = model.objects().get(pk=row_id)
    # record.delete()
    return redirect(reverse('technic:detail', args=(table_id, )))
