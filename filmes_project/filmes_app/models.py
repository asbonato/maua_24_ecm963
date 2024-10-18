from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    diretor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo