from django.db import models
from django.conf import settings
# Create your models here.

NULLABLE = {"blank": True, "null": True}

class Client(models.Model):
    email = models.EmailField(
        verbose_name = 'Почта для получения рассылки'
    )
    full_name = models.CharField(
        max_length = 150,
        verbose_name = 'ФИО',
        **NULLABLE
    )
    comment = models.TextField(
        verbose_name = 'Комментарий',
        **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        verbose_name = 'Владелец'
    )

    def __str__(self):
        return f'{self.full_name} - {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Newsletter(models.Model):
    PERIOD_DAILY = "daily"
    PERIOD_WEEKLY = "weekly"
    PERIOD_MONTHLY = "monthly"

    PERIOD_CHOICES = (
        (PERIOD_DAILY, "Ежедневно"),
        (PERIOD_WEEKLY, "Еженедельно"),
        (PERIOD_MONTHLY, "Ежемесячно"),
    )

    STATUS_CREATED = "created"
    STATUS_STARTED = "started"
    STATUS_DONE = "done"

    STATUS_CHOICES = (
        (STATUS_CREATED, "Создана"),
        (STATUS_STARTED, "Запущена"),
        (STATUS_DONE, "Завершена"),
    )

    date_started = models.DateTimeField(
        verbose_name = 'Дата начала рассылки'
    )
    date_finished = models.DateTimeField(
        verbose_name = 'Дата окончания рассылки',
        **NULLABLE
    )
    periodicity = models.CharField(
        max_length = 50,
        verbose_name = 'Периодичность рассылки',
        choices = PERIOD_CHOICES,
        default = PERIOD_DAILY
    )
    status = models.CharField(
        max_length = 50,
        verbose_name = 'Статус рассылки',
        choices = STATUS_CHOICES,
        default = STATUS_CREATED
    )
    message = models.ForeignKey(
        'Message',
        on_delete = models.CASCADE,
        verbose_name = 'Сообщения',
        **NULLABLE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        verbose_name = 'Владелец'
    )
    clients = models.ManyToManyField(
        Client,
        verbose_name = 'Клиенты'
    )

    def __str__(self):
        return f'{self.date_started} / {self.periodicity}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        permissions = [
            ('can_view_any_mailings', 'Can view any mailings'),
            ('can_disable_mailings', 'Can disable mailings'),
            ('can_view_the_list_of_service_users', 'Can view the list of service users'),
            ('can_block_users_of_the_service', 'Can block users of the service')
        ]

class Message(models.Model):
    subject_letter = models.CharField(
        max_length=150,
        verbose_name='Тема сообщения'
    )
    body_letter = models.TextField(
        verbose_name='Тело письма'
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Владелец'
    )

    def __str__(self):
        return self.subject_letter

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class MailingAttempt(models.Model):
    STATUS_OK = "success"
    STATUS_FAILED = "failed"
    STATUS_CHOICES = (
        (STATUS_OK, "Успешно"),
        (STATUS_FAILED, "Не успешно"),
    )

    date_last_attemp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата последнего попытки отправки'
    )
    status = models.CharField(
        max_length=50,
        verbose_name='Статус попытки отправки',
        choices=STATUS_CHOICES,
        default=STATUS_OK
    )
    service_response = models.CharField(
        max_length=200,
        verbose_name='Ответ почтового сервиса',
        **NULLABLE
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Клиент',
        **NULLABLE
    )
    settings = models.ForeignKey(
        Newsletter,
        on_delete=models.CASCADE,
        verbose_name='Настройки рассылки',
        **NULLABLE
    )

    class Meta:
        verbose_name = 'Попытка отправки рассылки'
        verbose_name_plural = 'Попытки отправки рассылок'
