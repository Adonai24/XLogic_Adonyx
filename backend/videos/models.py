from django.db import models

class Video(models.Model):

    CATEGORIAS = [
        ('programacion', 'Programación'),
        ('circuitos', 'Circuitos'),
        ('bases_datos', 'Bases de Datos'),
        ('sistemas', 'Sistemas Operativos'),
    ]
    titulo = models.CharField(max_length=200)

    archivo = models.FileField(upload_to='videos/')

    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    def __str__(self):
        return self.titulo
    