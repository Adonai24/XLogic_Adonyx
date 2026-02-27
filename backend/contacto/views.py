from django.shortcuts import render, redirect
from .models import MensajeContacto

def contacto(request):

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        MensajeContacto.objects.create(
            nombre=nombre,
            email=email,
            mensaje=mensaje
        )

        return redirect('contacto')

    return render(request, "contacto/Contacto.html")