# Generated by Django 4.2.14 on 2024-08-06 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='letter',
            options={'verbose_name': 'Letter', 'verbose_name_plural': 'Letters'},
        ),
        migrations.AlterModelOptions(
            name='mail',
            options={'verbose_name': 'Mail', 'verbose_name_plural': 'Mails'},
        ),
        migrations.AlterModelOptions(
            name='mailinglog',
            options={'verbose_name': 'MailingLog', 'verbose_name_plural': 'MailingLogs'},
        ),
        migrations.AlterField(
            model_name='mail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
