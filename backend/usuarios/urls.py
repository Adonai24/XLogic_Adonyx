from django.urls import path
from . import views

urlpatterns = [
    path('usuario/<str:nombre>/', views.saludo_usuario, name='saludo_usuario'),
]