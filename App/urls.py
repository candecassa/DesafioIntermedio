from django.urls import path
from .views import *


urlpatterns = [
    path('curso/', curso, name='curso'),
    path('estudiante/', estudiante, name='estudiante'),
    path('profesor/', profesor, name='profesor'),
    path('inicio/', inicio, name='inicio'),
    path('buscar/', buscar, name='buscar'),
    path('entregable/', entregable, name='entregable'),
    
]