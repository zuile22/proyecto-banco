from django.db import router
from rest_framework import routers, urlpatterns, views
from django.urls import path, include
from . import views
router = routers.DefaultRouter()


urlpatterns = [
    path('', views.star ,name = '' ),
    path('admin', views.admin,name='admin'),
    path('formulario', views.formulario ,name = 'formulario' ),
    path('consultar_solicitud', views.consultar_solicitud, name='consultar_solicitud'),
]