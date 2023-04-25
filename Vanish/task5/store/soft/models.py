from django.db import models

# Create your models here.


class Software(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    slogan = models.CharField(max_length=350, verbose_name="Слоган")
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Программное обеспечение'
        verbose_name_plural = 'Порграммные обеспечения'

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class SoftwareCompany(models.Model):
    software = models.ForeignKey('Software', on_delete=models.CASCADE, verbose_name="Программное обеспечение")
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name="Компания")

    class Meta:
        verbose_name = 'ПО - Компания'
        verbose_name_plural = 'ПО - Компании'

    def __str__(self):
        return f'{Software.objects.get(pk=self.software_id)}: {Company.objects.get(pk=self.company_id)}'

