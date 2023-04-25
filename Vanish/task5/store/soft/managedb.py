import datetime
from .models import Software, Company, SoftwareCompany


def select_all_from(model):
    return model.objects.all().values()


def add_record(model, params):
    record = model(*params)
    record.save()


def delete_record(model, row_id):
    record = model.objects.get(pk=row_id)
    record.delete()