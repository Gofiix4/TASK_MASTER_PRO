import os
import django
from django.contrib.auth.hashers import make_password
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "APITESCHI.settings")
django.setup()
from api.models import User, Status, Prioridad
datosAdmin = {'first_name': 'Carlos Enrique',
     'last_name': 'Hernandez Tellez',
     'is_superuser': True,
     'email': 'carlos.eht.09@gmail.com',
     'username': 'carloseht',
     'password': '123'}
datosAdmin['password'] = make_password(datosAdmin['password'])
datosStatus = [
    {'Status': 'Activo'},
    {'Status': 'Pendiente'},
    {'Status': 'Completada'},
    {'Status': 'Vencida'},
    {'Status': 'Cancelada'},
]
datosPrioridad = [
    {'Prioridad': 'Baja'},
    {'Prioridad': 'Media'},
    {'Prioridad': 'Alta'},
    {'Prioridad': 'Urgente'},
    {'Prioridad': 'Critica'},
    {'Prioridad': 'Inmediata'},
    {'Prioridad': 'Sin prioridad'},
]
createAdmin = User(**datosAdmin)
createAdmin.save()
print("Admin insertado correctamente.")
for datoStatus in datosStatus:
    createStatus = Status(**datoStatus)
    createStatus.save()
print("Status insertados correctamente.")
for datoPrioridad in datosPrioridad:
    createPrioridad = Prioridad(**datoPrioridad)
    createPrioridad.save()
print("Prioridad insertados correctamente.")

