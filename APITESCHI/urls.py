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
from api.views import Home, Signin, Signup, Signout, Pages, updPassword, Task, Icon, Starter, Table, forgotPwd, Error
from api import views

handler404 = 'api.views.page_not_found'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('chart/', views.chart_data, name='chart_data'),
    path('',Home.as_view(),name='index'),
    path('signin/',Signin.as_view(), name='signin'),
    path('signup/',Signup.as_view(), name='signup'),
    path('logout/',Signout.as_view(), name='logout'),
    path('pages/',Pages.as_view(),name='pages'),
    path('updatePwd/',updPassword.as_view(),name='update'),
    path('task/',Task.as_view(),name='task'),
    path('error/',Error.as_view(),name='error'),
    path('icon/',Icon.as_view(),name='icon'),
    path('starter/',Starter.as_view(),name='starter'),
    path('table/',Table.as_view(),name='table'),
    path('forgot-password/',forgotPwd.as_view(), name='forgot-password'),
    path('enviar_correo/<str:nombre>/<str:correo>/<str:apellido>/<str:usuario>/<str:contra>/<str:asunto>/<str:detalles>/', views.enviar_correo, name='enviar_correo'),
    path('weather/', views.weather, name='weather'),
]
