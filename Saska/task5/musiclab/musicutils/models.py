from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="Имя")
    last_name = models.CharField(max_length=250, verbose_name="Фамилия")
    playlist_size = models.IntegerField(verbose_name="Треков добавлено", default=0)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Album(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    pab_date = models.DateField(verbose_name="Дата публикации")

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name="Альбом")
    title = models.CharField(max_length=250, verbose_name="Название")
    singer = models.CharField(max_length=250, verbose_name="Исполнитель")
    duration = models.TimeField(verbose_name="Продолжительность")

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        return self.title


class UserPlaylist(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Пользователь")
    track = models.ForeignKey('Track', on_delete=models.CASCADE, verbose_name="Трек")

    class Meta:
        verbose_name = 'Плей-лист пользователя'
        verbose_name_plural = 'Плей-листы пользователей'

    def __str__(self):
        return f'{User.objects.get(pk=self.user_id)}: {Track.objects.get(pk=self.track_id)}'