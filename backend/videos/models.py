from django.db import models

class Video(models.Model):

    CATEGORIAS = [
        ('programacion', 'Programación'),
        ('circuitos', 'Circuitos'),
        ('bases_datos', 'Bases de Datos'),
        ('sistemas', 'Sistemas Operativos'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    youtube_url = models.URLField()

    def __str__(self):
        return self.titulo