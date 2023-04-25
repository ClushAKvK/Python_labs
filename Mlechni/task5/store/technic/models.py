from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="Имя")
    last_name = models.CharField(max_length=250, verbose_name="Фамилия")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Electronic(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    manufacturer = models.CharField(max_length=250, verbose_name="Производитель")
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Электроника'
        verbose_name_plural = 'Электроника'

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Пользователь")
    electronic = models.ForeignKey('Electronic', on_delete=models.CASCADE, verbose_name="Электроника")

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{User.objects.get(pk=self.user_id)}: {Electronic.objects.get(pk=self.electronic_id)}'

