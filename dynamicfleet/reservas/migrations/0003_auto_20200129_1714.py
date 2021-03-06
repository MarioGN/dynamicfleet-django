# Generated by Django 3.0.2 on 2020-01-29 17:14

import datetime
from django.db import migrations, models
import dynamicfleet.reservas.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reserve_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='start',
            field=models.DateTimeField(default=datetime.datetime.now, validators=[dynamicfleet.reservas.validators.validate_start_date], verbose_name='Inicio'),
        ),
    ]
