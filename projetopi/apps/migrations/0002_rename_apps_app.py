# Generated by Django 3.2.9 on 2021-11-25 09:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Apps',
            new_name='App',
        ),
    ]
