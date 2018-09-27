# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170827_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('Nombre_cl', models.CharField(max_length=25)),
                ('Apellido_cl', models.CharField(max_length=25)),
                ('Direccion_cl', models.CharField(max_length=20)),
                ('Telefono_cl', models.CharField(max_length=25)),
                ('Nit_cl', models.CharField(max_length=11)),
            ],
        ),
    ]
