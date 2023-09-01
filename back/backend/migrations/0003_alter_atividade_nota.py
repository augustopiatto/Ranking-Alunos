# Generated by Django 4.2.4 on 2023-09-01 16:35

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_escola_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[backend.models.validate_interval]),
        ),
    ]
