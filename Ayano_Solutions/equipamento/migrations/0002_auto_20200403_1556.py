# Generated by Django 3.0.5 on 2020-04-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='edataC',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='emanutencao',
            field=models.CharField(max_length=3),
        ),
    ]
