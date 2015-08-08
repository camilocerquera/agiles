from django.db import models

class Imagen(models.Model):
    nombre = models.CharField(max_length = 200)
    url = models.CharField(max_length = 1000)
    def __str__(self):
        return self.nombre+" "+self.url
