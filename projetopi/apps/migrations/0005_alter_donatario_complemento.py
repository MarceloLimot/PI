# Generated by Django 3.2.9 on 2021-11-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_donatario_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donatario',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
