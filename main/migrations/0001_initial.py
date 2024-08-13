# Generated by Django 4.2.14 on 2024-08-05 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('about', models.TextField(verbose_name='комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('let_about', models.CharField(max_length=100, verbose_name='тема рассылки')),
                ('let_text', models.TextField(verbose_name='текс рассылки')),
            ],
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='время последней попыткм рассылки')),
                ('status', models.CharField(choices=[('success', 'успешно'), ('fail', 'не доставлено'), ('error', 'ошибка')], max_length=20, verbose_name='статус последней попытки расслыки')),
                ('answer', models.CharField(blank=True, max_length=100, null=True, verbose_name='ответ сервера')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.client', verbose_name='клиенты')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.letter', verbose_name='сообщение')),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='имя рассылки')),
                ('mail_time', models.DateTimeField(verbose_name='время рассылки')),
                ('mail_regularity', models.CharField(choices=[('Ежедневно', 'Ежедневно'), ('Еженедельно', 'Еженедельно'), ('Ежемесячно', 'Ежемесячно')], max_length=40, verbose_name='регулярность')),
                ('mail_status', models.CharField(choices=[('Создана', 'Создана'), ('Запущена', 'Запущена'), ('Завершена', 'Завершена')], max_length=40, verbose_name='статус расслыки')),
                ('clients', models.ManyToManyField(blank=True, related_name='clients', to='main.client', verbose_name='клиенты')),
                ('message', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.letter')),
            ],
        ),
    ]
