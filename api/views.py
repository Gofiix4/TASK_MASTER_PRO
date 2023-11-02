from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Cadena aleatoria
import secrets
import string
#
from django.http import HttpResponse
from user_agents import parse
import user_agents 

import datetime
# Create your views here.
from .models import Encuesta_calidad

class Home(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Signup(APIView):
    template_name="signup.html"
    def get(self,request):
        return render(request, self.template_name,{
            'form' : UserCreationForm
        })
    def post(self,request):
        longitud = 10
        caracteres = string.ascii_letters + string.digits
        contra_aleatoria = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        try:
            correo = User.objects.filter(email=request.POST['email'])
            if correo.exists():
                return render(request, self.template_name, {
                    'form' : UserCreationForm,
                    "mensaje" : 'El email que ingresaste ya es utilizado por otra persona, prueba introduciendo otro'
                })
            else:
                # Aqui guarda en la base de datos
                user = User.objects.create_user(first_name=request.POST['first_name'], email=request.POST['email'], last_name=request.POST['last_name'], username=request.POST['username'], password=contra_aleatoria) # Al final a password se le asigna el valor de contraseña aleatoria
                # Guardas el usuario
                user.save()
                # Defines variables para que posteriormente las mandes por una mamada de link inverso xd a la clase que manda el correo
                nombre = request.POST['first_name']
                correo = request.POST['email']
                apellido = request.POST['last_name']
                usuario = request.POST['username']
                asunto = 'Bienvenida'
                detalles = 'Bienvenido a Task Master Pro, tu compañero confiable en la gestión de tareas y la organización de tu vida diaria. Estamos encantados de que te hayas unido a nuestra comunidad de usuarios dedicados a mejorar su productividad y simplificar sus días.'
                # Igual aqui a contra le mandas el valor de la cadena generada automaticamente
                contra = contra_aleatoria
                # Aqui retorna a la clase de enviar correo
                return redirect('enviar_correo', nombre=nombre, correo=correo, apellido=apellido, usuario=usuario, contra=contra, asunto=asunto, detalles=detalles)
            # Aqui te regresa al mismo formulario si es que el usuario que ingresaste ya existe
        except IntegrityError:
            return render(request, self.template_name, {
                'form' : UserCreationForm,
                "mensaje" : 'El usuario que ingresaste ya es utilizado por otra persona, prueba introduciendo otro'
            })
        except MultiValueDictKeyError:
            return render(request, self.template_name, {
                'form': AuthenticationForm,
                'mensaje': 'Alguno de los campos no han sido llenados de manera correcta, intentalo de nuevo'
            })

class Signin(APIView):
    template_name="signin.html"
    def get(self,request):
        return render(request, self.template_name, {
            'form': AuthenticationForm
        })
    def post(self,request):
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, self.template_name, {
                    'form': AuthenticationForm,
                    'error': 'Usuario o contraseña incorrecta'
                })
            else:
                user = User.objects.filter(username=request.POST['username'])
                user = user[0]
                nombre = user.first_name
                correo = user.email
                login(request, user)
                nombre = nombre
                correo = correo
                apellido = " "
                usuario = " "
                contra = " "
                asunto = 'Inicio de sesión'
                detalles = 'Te informamos que se ha detectado un inicio de sesión en tu cuenta de Task Master Pro. Creemos en la importancia de mantener tu cuenta segura y deseamos mantenerte informado sobre cualquier actividad en tu cuenta.'
                return redirect('enviar_correo', nombre=nombre, correo=correo, apellido=apellido, usuario=usuario, contra=contra, asunto=asunto, detalles=detalles)
        except MultiValueDictKeyError:
            return render(request, self.template_name, {
                    'form': AuthenticationForm,
                    'error': 'Alguno de los campos no han sido llenados de manera correcta, intentalo de nuevo'
                })
        except IntegrityError:
            return render(request, self.template_name, {
                'form' : UserCreationForm,
                "mensaje" : 'No se ha podido iniciar sesión de manera coorrecta, intentalo de nuevo'
            })
            
class Signout(APIView):
    def get(self,request):
        logout(request)
        return redirect('signin')

class Error(APIView):
    template_name="error-404.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Icon(APIView):
    template_name="icon-material.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Pages(APIView):
    template_name="pages-profile.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Starter(APIView):
    template_name="starter-kit.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Table(APIView):
    template_name="table-basic.html"
    def get(self,request):
        usuarios = User.objects.all()  # Obtén todos los registros de la tabla auth_user
        return render(request, 'table-basic.html', {'usuarios': usuarios})
    def post(self,request):
        return render(request,self.template_name)



def enviar_correo(request, nombre, correo, apellido, usuario, contra, asunto, detalles):
    subject = asunto
    from_email = 'carlos.eht.09@gmail.com'
    recipient_list = [correo]
    # Se utiliza una variable para guardar la informacion del dispositivo que se esta usando
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    # Ejecuta un if else para revisar que tipo de dispositivo es, y se le asigna el valor a la variable "dispositivo"
    if user_agent.is_mobile:
        dispositivo = 'Móvil'
    elif user_agent.is_tablet:
        dispositivo = 'Tablet'
    else:
        dispositivo = 'PC'
    # Ahora con un if else verifica si se obtuvo informacion del navegador
    if user_agent.browser.family:
        # Si encuentra informacion guarda su nombre y su version
        browser_name = user_agent.browser.family
        browser_version = user_agent.browser.version_string
    else:
        # Si no, se le guarda un texto en la variables
        browser_name = 'No se pudo detectar'
        browser_version = 'No se pudo detectar'
    # Ahora obtiene la IP
    client_ip = request.META.get('REMOTE_ADDR')
    # Aqui obtiene la fecha y hora actual
    current_datetime = datetime.datetime.now()
    # En la variable se guarda la fecha y hora ya con un formato
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    # Renderiza la plantilla HTML con el contexto
    contexto = {'nombre': nombre,
                'correo': correo,
                'apellido': apellido,
                'usuario': usuario,
                'contra': contra,
                'asunto': asunto,
                'detalles': detalles,
                'dispositivo': dispositivo,
                'ip': client_ip,
                'navegador': browser_name,
                'version': browser_version,
                'fecha': formatted_datetime}
    contenido_correo = render_to_string('email.html', contexto)

    # Envía el correo
    send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)
    # Redirige al inicio de sesion
    return redirect('/')

class forgotPwd(APIView):
    template_name="forgot_password.html"
    def get(self,request):
        return render(request, self.template_name,{
            'form' : UserCreationForm
        })
    def post(self,request):
        longitud = 10  # Longitud de la contraseña
        caracteres = string.ascii_letters + string.digits  # Caracteres permitidos
        contra_aleatoria = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        try:
            user = User.objects.filter(email=request.POST['email'])
            if user.exists():
                user = user[0]
                nombre = user.first_name
                usuario = user.username
                user.set_password(contra_aleatoria)
                user.save()
                # Defines variables para que posteriormente las mandes por una mamada de link inverso xd a la clase que manda el correo
                nombre = nombre
                correo = request.POST['email']
                apellido = " "
                usuario = usuario
                asunto = "Reestablecer contraseña"
                detalles = 'Hemos recibido tu solicitud para restablecer tu contraseña en Task Master Pro. Tu seguridad es nuestra prioridad, y estamos aquí para ayudarte a recuperar el acceso a tu cuenta, es por eso que te hemos asignado una nueva contraseña para que puedas tener acceso nuevamente.'
                # Igual aqui a contra le mandas el valor de la cadena generada automaticamente
                contra = contra_aleatoria
                # Aqui retorna a la clase de enviar correo
                return redirect('enviar_correo', nombre=nombre, correo=correo, apellido=apellido, usuario=usuario, contra=contra, asunto=asunto, detalles=detalles)
            else:
                return render(request, self.template_name,{
                    'form' : UserCreationForm,
                    "mensaje" : 'No hemos podido localizar tu cuenta, asegurate de que tu correo sea correcto'
                })
        except IntegrityError:
            return render(request, self.template_name,{
                'form' : UserCreationForm,
                "mensaje" : 'No hemos podido localizar tu cuenta, asegurate de que tu correo sea correcto'
            })

def chart_data(request):
    ventas = Encuesta_calidad.objects.all()
    # Procesa los datos y prepáralos para el gráfico
    data = {
        'labels': [str(venta.Pregunta2) for venta in ventas],
        'data': [venta.Pregunta2 for venta in ventas],
    }
    return render(request, 'chart.html', {'data': data})

def page_not_found(request, exception):
    return render(request, 'error-404.html', status=404)