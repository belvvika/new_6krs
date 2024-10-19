from django.db import models

# Create your models here.

from users.models import User

NULLABLE = {"blank": True, "null": True}
class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок',
        help_text='Введите заголовок блога'
    )
    content = models.TextField(
        verbose_name='Содержание',
        help_text='Введите текст блога'
    )
    publish_at = models.DateField(
        verbose_name='Дата публикации',
        help_text='Введите дату публикации',
        blank=True,
        null=True
    )
    count_view = models.IntegerField(
        verbose_name='Количество просмотров',
        default=0,
        help_text='Счетчик просмотров'
    )
    photo = models.ImageField(
        upload_to='blogs/photo',
        blank=True,
        null=True,
        verbose_name='Фотография',
        help_text='Загрузите фотографию блога'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Выберите пользователя',
        **NULLABLE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'