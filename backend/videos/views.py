from django.shortcuts import render
from .models import Video

def inicio(request):

    return render(request,'videos/Index.html')


def sobre_mi(request):

    return render(request,'videos/Sobre_Mi.html')


def contacto(request):

    return render(request,'videos/Contacto.html')


def videos(request):

    videos = Video.objects.all()

    return render(request,"videos/videos.html",{
        "videos":videos
    })
    
    