# Generated by Django 2.2 on 2019-05-09 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ejecucion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstory',
            name='usuario_asignado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, to_field='id'),
        ),
    ]