"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from shooter import views 
from shooter.views import index 
from django.conf import settings
from shooter.views import int_tir
from shooter.views import laser_tir
from shooter.views import panarama
from shooter.views import btr
from shooter.views import desant
from shooter.views import dpm
from shooter.views import mobil
from shooter.views import pzrk
from shooter.views import vr

urlpatterns = [
    path('', index),
    path('template', views.int_tir, name='int_tir'),
    path('lasertir', views.laser_tir, name='laser_tir'),
    path('panaroma', views.panarama, name='panarama'),
    path('btr', views.btr, name='btr'),
    path('desant', views.desant, name='desant'),
    path('dpm', views.dpm, name='dpm'),
    path('mobil', views.mobil, name='mobil'),
    path('pzrk', views.pzrk, name='pzrk'),
    path('vr', views.vr, name='vr'),
    path('start_bot', views.start_bot),
   ]
