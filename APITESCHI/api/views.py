from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Cadena aleatoria
import secrets
import string
#
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class Home(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

class Signup(APIView):
    template_name="signup.html"
    def get(self,request):
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    def post(self,request):
        longitud = 10  # Longitud de la contraseña
        caracteres = string.ascii_letters + string.digits  # Caracteres permitidos
        contra_aleatoria = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        try:
            # Aqui guarda en la base de datos
            user = User.objects.create_user(first_name=request.POST['first_name'], email=request.POST['email'], last_name=request.POST['last_name'], username=request.POST['username'], password=contra_aleatoria) # Al final a password se le asigna el valor de contraseña aleatoria
            # Guardas el usuario
            user.save()
            # Defines variables para que posteriormente las mandes por una mamada de link inverso xd a la clase que manda el correo
            nombre = request.POST['first_name']
            correo = request.POST['email']
            apellido = request.POST['last_name']
            usuario = request.POST['username']
            # Igual aqui a contra le mandas el valor de la cadena generada automaticamente
            contra = contra_aleatoria
            # Aqui retorna a la clase de enviar correo
            return redirect('enviar_correo', nombre=nombre, correo=correo, apellido=apellido, usuario=usuario, contra=contra)
        # Aqui te regresa al mismo formulario si es que el usuario que ingresaste ya existe
        except IntegrityError:
            return render(request, 'signup.html',{
                'form' : UserCreationForm,
                "mensaje" : 'Este usuario ya existe, por favor ingresa otro'
            })

class Signin(APIView):
    template_name="signin.html"
    def get(self,request):
        return render(request, self.template_name, {
            'form': AuthenticationForm
        })
    def post(self,request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, self.template_name, {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect("/")
            
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

#Envio del correo



def enviar_correo(request, nombre, correo, apellido, usuario, contra):
    subject = 'Bienvenida'
    from_email = 'carlos.eht.09@gmail.com'
    recipient_list = [correo]

    # Renderiza la plantilla HTML con el contexto
    contexto = {'nombre': nombre,
                'correo': correo,
                'apellido': apellido,
                'usuario': usuario,
                "contra": contra}
    contenido_correo = render_to_string('base_correo.html', contexto)

    # Envía el correo
    send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)
    
    return redirect('signin')

def forgotPwd(request):
    longitud = 10  # Longitud de la contraseña
    caracteres = string.ascii_letters + string.digits  # Caracteres permitidos

    contra_aleatoria = ''.join(secrets.choice(caracteres) for _ in range(longitud)) # Generacion de la contraseña
    # Si esta solicitando informacion por el metodo GET se envia el formulario
    if request.method =='GET':
        return render(request, 'forgot_password.html',{
            'form' : UserCreationForm
        })
    # Si no, se esta posteando informacion
    else:
        try:
            user = User.objects.filter(email=request.POST['email'])
            if user.exists():
                user = user[0]
                user.set_password(contra_aleatoria)
                user.save()
            # Defines variables para que posteriormente las mandes por una mamada de link inverso xd a la clase que manda el correo
            nombre = " "
            correo = request.POST['email']
            apellido = " "
            usuario = " "
            # Igual aqui a contra le mandas el valor de la cadena generada automaticamente
            contra = contra_aleatoria
            # Aqui retorna a la clase de enviar correo
            return redirect('enviar_correo', nombre=nombre, correo=correo, apellido=apellido, usuario=usuario, contra=contra)
        # Aqui te regresa al mismo formulario si es que el usuario que ingresaste ya existe
        except IntegrityError:
            return render(request, 'forgot_password.html',{
                'form' : UserCreationForm,
                "mensaje" : 'Este usuario ya existe, por favor ingresa otro'
            })