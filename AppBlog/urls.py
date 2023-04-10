from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='inicio'),
    path('busqueda/', busqueda),
    path('registro/', registro, name='registro'),
    path('publicar-post/', posts, name='publicar-post'),
    path('comentarios/', comentarios, name='comentarios'),
]