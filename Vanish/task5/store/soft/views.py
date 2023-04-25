from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Software, Company, SoftwareCompany
from . import managedb, xml_soft
from django.apps import apps

# Create your views here.
models = apps.get_app_config('soft').get_models()
models = {idx: model for idx, model in enumerate(models)}


def index(request):

    # managedb.insert_data()

    ru_models = {idx: model._meta.verbose_name_plural.title() for idx, model in models.items()}
    content = {
        'models': ru_models
    }
    return render(request, 'soft/index.html', content)


def create_xml(request):
    xml_soft.create_xml(apps.get_app_config('soft').get_models())
    return redirect(reverse('soft:index'))


def detail(request, table_id):
    model = models[table_id]
    records = model.objects.all().values()
    fields = [f.verbose_name for f in model._meta.fields]

    for record in records:
        for key, val in record.items():
            if model._meta.model_name == 'softwarecompany':
                if key == 'software_id':
                    record[key] = Software.objects.get(pk=int(val)).name
                elif key == 'company_id':
                    record[key] = Company.objects.get(pk=int(val)).name

    content = {
        'records': records,
        'fields': fields,
        'model_name': model._meta.verbose_name_plural.title(),
        'table_id': table_id
    }

    if model._meta.model_name == 'softwarecompany':
        softwares = Software.objects.all()
        companys = Company.objects.all()

        content['softwares'] = softwares
        content['companys'] = companys

    return render(request, 'soft/detail.html', content)


def add_record(request, table_id):
    model = models[table_id]

    try:
        params = [model.objects.order_by('-id').first().id + 1]
    except AttributeError:
        params = [1]

    if model._meta.model_name == 'softwarecompany':
        params.append(request.POST['software'])
        params.append(request.POST['company'])
    else:
        for key, val in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                params.append(val)

    managedb.add_record(model, params)
    return redirect(reverse('soft:detail', args=(table_id,)))


def delete_record(request, table_id, row_id):
    model = models[table_id]
    # print(model.objects.get(pk=row_id))
    managedb.delete_record(model, row_id)
    # record = model.objects().get(pk=row_id)
    # record.delete()
    return redirect(reverse('soft:detail', args=(table_id, )))
