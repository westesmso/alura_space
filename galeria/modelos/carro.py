from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=100, null=False, blank=False)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    ano = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Carro [marca={self.marca}, modelo={self.modelo}, ano={self.ano}]"