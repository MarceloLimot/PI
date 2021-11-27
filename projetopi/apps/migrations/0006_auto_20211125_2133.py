# Generated by Django 3.2.9 on 2021-11-26 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_donatario_complemento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=15)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('Bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=100)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='loginfunc',
            old_name='usuario',
            new_name='nome',
        ),
        migrations.AddField(
            model_name='loginfunc',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='loginfunc',
            name='telefone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='donatario',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
