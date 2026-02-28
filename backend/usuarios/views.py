from django.shortcuts import render

def saludo_usuario(request, nombre):
    nombre_mayus = nombre.upper()
    return render(request, 'usuarios/usuario.html', {
        'nombre': nombre_mayus
    })