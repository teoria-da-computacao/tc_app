# Generated by Django 4.0.6 on 2024-06-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computacao', '0002_automato_diagrama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automato',
            name='diagrama',
            field=models.FileField(blank=True, null=True, upload_to='afd_diagrams/'),
        ),
    ]