# Generated by Django 2.2 on 2019-05-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_auto_20190509_1811'),
        ('ejecucion', '0002_auto_20190509_1811'),
        ('auth', '0011_update_proxy_permissions'),
        ('administracion', '0004_auto_20190509_1651'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='CustomUser',
        ),
    ]
