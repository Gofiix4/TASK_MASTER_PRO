from django.db import models
from django.contrib.auth.models import User

class Tareas(models.Model):
    idTarea = models.AutoField(primary_key=True,db_column='idTarea')
    Titulo = models.CharField(max_length=50,default='Titulo',db_column='Titulo')
    Descripcion = models.CharField(max_length=200,default='Descripcion',db_column='Descripcion')
    Fecha_creacion = models.DateField(default='2000-01-01',db_column='Fecha_creacion')
    Fecha_vencimiento = models.DateField(default='2000-01-01',db_column='Fecha_vencimiento')
    Status = models.CharField(max_length=15,default='Pendiente',db_column='Status')
    Prioridad = models.CharField(max_length=10,default='Baja',db_column='Prioridad')
    fk_Usuario = models.ForeignKey(User,on_delete=models.CASCADE,db_column='fk_Usuario')
    class Meta:
        db_table='Tareas'

class Lista_tareas(models.Model):
    idLista = models.AutoField(primary_key=True,db_column='idLista')
    Nombre = models.CharField(max_length=45,default='Nombre',db_column='Nombre')
    Descripcion = models.CharField(max_length=200,default='Descripcion',db_column='Descripcion')
    fk_Usuario = models.ForeignKey(User,on_delete=models.CASCADE,db_column='fk_Usuario')
    class Meta:
        db_table='Lista_tareas'

class Listas_has_tareas(models.Model):
    idListas_has_tareas = models.AutoField(primary_key=True,default=1,db_column='idListas_has_tareas')
    fk_Lista = models.ForeignKey(Lista_tareas,on_delete=models.CASCADE,db_column='fk_Lista')
    fk_Tarea = models.ForeignKey(Tareas,on_delete=models.CASCADE,db_column='fk_Tarea')
    class Meta:
        db_table='Listas_has_tareas'

class Etiquetas(models.Model):
    idEtiqueta = models.AutoField(primary_key=True,db_column='idEtiqueta')
    Nombre = models.CharField(max_length=20,default='Nombre',db_column='Nombre')
    Descripcion = models.CharField(max_length=100,default='Descripcion',db_column='Descripcion')
    class Meta:
        db_table='Etiquetas'

class Tareas_has_etiquetas(models.Model):
    idTareas_has_etiquetas = models.AutoField(primary_key=True,default=1,db_column='idTareas_has_etiquetas')
    fk_Tarea = models.ForeignKey(Tareas,on_delete=models.CASCADE,db_column='fk_Tarea')
    fk_Etiqueta = models.ForeignKey(Etiquetas,on_delete=models.CASCADE,db_column='fk_Etiqueta')
    class Meta:
        db_table='Tareas_has_etiquetas'
        
class Encuesta_calidad(models.Model):
    Marca_temporal = models.TextField(max_length=200, default='Marca temporal', db_column='Marca temporal')
    Pregunta1 = models.TextField(max_length=200, default='pregunta1', db_column='Satisfaccion de usabilidad')
    Pregunta2 = models.TextField(max_length=200, default='pregunta2', db_column='Frecuencia de uso')
    Pregunta3 = models.TextField(max_length=200, default='pregunta3', db_column='Caracteristica mas util')
    Pregunta4 = models.TextField(max_length=200, default='pregunta4', db_column='Caracteristica a mejorar')
    Pregunta5 = models.TextField(max_length=200, default='pregunta5', db_column='La recomendarias')
    Pregunta6 = models.TextField(max_length=200, default='pregunta6', db_column='Velocidad y rendimiento')
    Pregunta7 = models.TextField(max_length=200, default='pregunta7', db_column='Servicio de FAQ')
    class Meta:
        db_table='Encuesta_calidad'
    