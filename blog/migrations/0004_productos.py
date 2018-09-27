# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=25)),
                ('Descripcion', models.CharField(max_length=25)),
                ('Costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Cantidad', models.CharField(max_length=25)),
                ('Estado', models.BooleanField()),
            ],
        ),
    ]
