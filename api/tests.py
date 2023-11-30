import pytest
from django.contrib.auth.models import User
from .models import Tareas, Lista_tareas, Listas_has_tareas,Ciudades, Consultas, Favoritos
from datetime import date

@pytest.mark.django_db
def test_tareas_model():
    # Crear un usuario de prueba
    usuario = User.objects.create(username='test_user')

    # Crear una tarea
    tarea = Tareas.objects.create(
        Titulo='Prueba de tarea',
        Descripcion='Descripción de la tarea de prueba',
        Fecha_creacion=date(2023, 1, 1),
        Fecha_vencimiento=date(2023, 1, 31),
        Status='Pendiente',
        Prioridad='Alta',
        fk_Usuario=usuario,
    )

    # Obteniene la tarea desde la base de datos
    tarea_db = Tareas.objects.get(pk=tarea.idTarea)

    # Consulta datos de la tarea
    assert tarea_db.Titulo == 'Prueba de tarea'
    assert tarea_db.Descripcion == 'Descripción de la tarea de prueba'
    assert tarea_db.Fecha_creacion == date(2023, 1, 1)
    assert tarea_db.Fecha_vencimiento == date(2023, 1, 31)
    assert tarea_db.Status == 'Pendiente'
    assert tarea_db.Prioridad == 'Alta'
    assert tarea_db.fk_Usuario == usuario

    # Elimina la tarea
    tarea_db.delete()

@pytest.mark.django_db
def test_lista_tareas_model():
    # Crear un usuario de prueba
    usuario = User.objects.create(username='test_user')

    # Crear una lista de tareas
    lista_tareas = Lista_tareas.objects.create(
        Nombre='Lista de prueba',
        Descripcion='Descripción de la lista de prueba',
        fk_Usuario=usuario,
    )

    # Obtener la lista de tareas desde la base de datos
    lista_tareas_db = Lista_tareas.objects.get(pk=lista_tareas.idLista)

    # Consulta datos de la lista de tareas
    assert lista_tareas_db.Nombre == 'Lista de prueba'
    assert lista_tareas_db.Descripcion == 'Descripción de la lista de prueba'
    assert lista_tareas_db.fk_Usuario == usuario

    # Eliminar la lista de tareas
    lista_tareas_db.delete()


@pytest.mark.django_db
def test_listas_has_tareas_model():
    # Crear un usuario de prueba
    usuario = User.objects.create(username='test_user')

    # Crear una lista de tareas
    lista_tareas = Lista_tareas.objects.create(
        Nombre='Lista de prueba',
        Descripcion='Descripción de la lista de prueba',
        fk_Usuario=usuario,
    )

    # Crear una tarea
    tarea = Tareas.objects.create(
        Titulo='Prueba de tarea',
        Descripcion='Descripción de la tarea de prueba',
        Fecha_creacion=date(2023, 1, 1),
        Fecha_vencimiento=date(2023, 1, 31),
        Status='Pendiente',
        Prioridad='Alta',
        fk_Usuario=usuario,
    )

    # Asociar la tarea a la lista de tareas
    lista_tareas_has_tareas = Listas_has_tareas.objects.create(
        fk_Lista=lista_tareas,
        fk_Tarea=tarea,
    )

    # Obtener la relación desde la base de datos
    lista_tareas_has_tareas_db = Listas_has_tareas.objects.get(pk=lista_tareas_has_tareas.idListas_has_tareas)

    # Consulta datos de la relación
    assert lista_tareas_has_tareas_db.fk_Lista == lista_tareas
    assert lista_tareas_has_tareas_db.fk_Tarea == tarea

    # Eliminar la relación
    lista_tareas_has_tareas_db.delete()
    tarea.delete()
    lista_tareas.delete()

