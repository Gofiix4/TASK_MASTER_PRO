from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class Home(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)

def signup(request):
    if request.method =='GET':
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(first_name=request.POST['first_name'], email=request.POST['email'], last_name=request.POST['last_name'], username=request.POST['username'], password=request.POST['password1'])
                user.save()
                nombre = request.POST['first_name']
                correo = request.POST['email']
                apellido = request.POST['last_name']
                usuario = request.POST['username']
                contra = request.POST['password1']
                return redirect('enviar_correo', nombre=nombre, correo=correo, apellido=apellido, usuario=usuario, contra=contra)
                
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    "mensaje" : 'Este usuario ya existe, por favor ingresa otro'
                })
                #return HttpResponse('Username already exist')
        return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    "mensaje" : 'Ambas contraseñas no coinciden'
                })  
        #return HttpResponse('Password do not match')
def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect("/")

"""
class Signin(APIView):
    template_name="signin.html"
    def get(self,request):
        print('Enviando formulario')
        return render(request,self.template_name)
    def post(self,request):
        print('Obteniendo datos')
        return render(request,self.template_name)

class Signup(APIView):
    template_name="signup.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)
"""
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
        return render(request,self.template_name)
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