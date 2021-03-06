# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('idVendedor', models.IntegerField(default=0)),
                ('nombre', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('categorias', multiselectfield.db.fields.MultiSelectField(choices=[(0, 'Cerdo'), (1, 'Chino'), (2, 'Completos'), (3, 'Egipcio'), (4, 'Empanadas'), (5, 'Ensalada'), (6, 'Japones'), (7, 'Pan'), (8, 'Papas fritas'), (9, 'Pasta'), (10, 'Pescado'), (11, 'Pollo'), (12, 'Postres'), (13, 'Sushi'), (14, 'Vacuno'), (15, 'Vegano'), (16, 'Vegetariano')], max_length=40)),
                ('descripcion', models.CharField(max_length=500)),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('precio', models.PositiveSmallIntegerField(default=0)),
                ('imagen', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'Comida',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('tipo', models.IntegerField(choices=[(0, 'admin'), (1, 'alumno'), (2, 'fijo'), (3, 'ambulante')])),
                ('avatar', models.CharField(max_length=200)),
                ('contraseña', models.CharField(max_length=200)),
                ('activo', models.BooleanField()),
                ('formasDePago', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'Tarjeta'), (1, 'Efectivo')], max_length=3)),
                ('horario', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
