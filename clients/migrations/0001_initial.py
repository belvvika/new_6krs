# Generated by Django 5.1.2 on 2024-10-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта для получения рассылки')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='ФИО')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_last_attemp', models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего попытки отправки')),
                ('status', models.CharField(choices=[('success', 'Успешно'), ('failed', 'Не успешно')], default='success', max_length=50, verbose_name='Статус попытки отправки')),
                ('service_response', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ответ почтового сервиса')),
            ],
            options={
                'verbose_name': 'Попытка отправки рассылки',
                'verbose_name_plural': 'Попытки отправки рассылок',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_letter', models.CharField(max_length=150, verbose_name='Тема сообщения')),
                ('body_letter', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField(verbose_name='Дата начала рассылки')),
                ('date_finished', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания рассылки')),
                ('periodicity', models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], default='daily', max_length=50, verbose_name='Периодичность рассылки')),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Запущена'), ('done', 'Завершена')], default='created', max_length=50, verbose_name='Статус рассылки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'permissions': [('can_view_any_mailings', 'Can view any mailings'), ('can_disable_mailings', 'Can disable mailings'), ('can_view_the_list_of_service_users', 'Can view the list of service users'), ('can_block_users_of_the_service', 'Can block users of the service')],
            },
        ),
    ]
