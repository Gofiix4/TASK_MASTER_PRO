# Generated by Django 3.2.4 on 2023-10-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta_calidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca_temporal', models.TextField(db_column='Marca temporal', default='Marca temporal', max_length=200)),
                ('Pregunta1', models.TextField(db_column='Satisfaccion de usabilidad', default='pregunta1', max_length=200)),
                ('Pregunta2', models.TextField(db_column='Frecuencia de uso', default='pregunta2', max_length=200)),
                ('Pregunta3', models.TextField(db_column='Caracteristica mas util', default='pregunta3', max_length=200)),
                ('Pregunta4', models.TextField(db_column='Caracteristica a mejorar', default='pregunta4', max_length=200)),
                ('Pregunta5', models.TextField(db_column='La recomendarias', default='pregunta5', max_length=200)),
                ('Pregunta6', models.TextField(db_column='Velocidad y rendimiento', default='pregunta6', max_length=200)),
                ('Pregunta7', models.TextField(db_column='Servicio de FAQ', default='pregunta7', max_length=200)),
            ],
            options={
                'db_table': 'Encuesta_calidad',
            },
        ),
    ]