# Generated by Django 3.0.2 on 2020-01-29 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0002_auto_20200128_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('disponivel', 'Disponível'), ('manutencao', 'Manutenção')], default='disponivel', max_length=10, verbose_name='Status'),
        ),
    ]
