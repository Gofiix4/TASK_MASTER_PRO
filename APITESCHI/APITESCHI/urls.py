"""APITESCHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import Home, Icon, Pages, Starter, Table
from api.views import Error
from api import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    #path('signin/',Signin.as_view(),name='signin'),
    #path('signup/',Signup.as_view(),name='signup'),
    path('error/',Error.as_view(),name='error'),
    path('icon/',Icon.as_view(),name='icon'),
    path('pages/',Pages.as_view(),name='pages'),
    path('starter/',Starter.as_view(),name='starter'),
    path('table/',Table.as_view(),name='table'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('forgot-password/',views.forgotPwd, name='forgot-password'),
    path('enviar_correo/<str:nombre>/<str:correo>/<str:apellido>/<str:usuario>/<str:contra>/', views.enviar_correo, name='enviar_correo'),
    
]
