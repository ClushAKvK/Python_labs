from django.db import models

# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.CharField(max_length=350, verbose_name="Описание")
    chance_to_survive = models.IntegerField(verbose_name="Шанс выжить", default=0)

    class Meta:
        verbose_name = 'Заболевание'
        verbose_name_plural = 'Заболевания'

    def __str__(self):
        return self.name


class Symptom(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = 'Симптом'
        verbose_name_plural = 'Симптомы'

    def __str__(self):
        return self.name


class DiseaseSymptom(models.Model):
    disease = models.ForeignKey('Disease', on_delete=models.CASCADE, verbose_name="Заболевание")
    symptom = models.ForeignKey('Symptom', on_delete=models.CASCADE, verbose_name="Симптом")

    class Meta:
        verbose_name = 'Симптом - болезнь'
        verbose_name_plural = 'Симптомы - болезни'

    def __str__(self):
        return f'{Disease.objects.get(pk=self.disease_id)}: {Symptom.objects.get(pk=self.symptom_id)}'

