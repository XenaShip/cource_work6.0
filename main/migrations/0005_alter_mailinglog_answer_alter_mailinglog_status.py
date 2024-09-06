# Generated by Django 4.2.14 on 2024-08-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_mail_mail_time_mail_mail_time_finish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailinglog',
            name='answer',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='ответ сервера'),
        ),
        migrations.AlterField(
            model_name='mailinglog',
            name='status',
            field=models.CharField(choices=[('success', 'успешно'), ('error', 'ошибка')], max_length=20, verbose_name='статус последней попытки расслыки'),
        ),
    ]
