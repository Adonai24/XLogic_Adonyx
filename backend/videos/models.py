import re
from django.db import models

class Video(models.Model):

    CATEGORIAS = [
        ('programacion', 'Programación'),
        ('circuitos', 'Circuitos'),
        ('bases_datos', 'Bases de Datos'),
        ('sistemas', 'Sistemas Operativos'),
    ]

    titulo = models.CharField(max_length=200)

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

    youtube_url = models.URLField("Link de YouTube")

    youtube_id = models.CharField(max_length=20, blank=True)


    def save(self, *args, **kwargs):

        url = self.youtube_url

        regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
        match = re.search(regex, url)

        if match:
            self.youtube_id = match.group(1)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.titulo