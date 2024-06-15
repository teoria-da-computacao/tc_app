# Generated by Django 3.2 on 2021-04-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('alfabeto', models.CharField(max_length=100)),
                ('estados', models.CharField(max_length=100)),
                ('estadoInicial', models.CharField(max_length=100)),
                ('estadosDeAceitacao', models.CharField(max_length=100)),
                ('dicionarioTransicao', models.CharField(max_length=1000)),
            ],
        ),
    ]
