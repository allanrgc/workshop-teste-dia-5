from django.db import models

class Autor(models.Model):
    autor = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.autor}'

class Livraria(models.Model):
    nome = models.CharField(max_length=40)
    preco = models.CharField(max_length=20)
    autor = models.ForeignKey(
        Autor,
        max_length=20,
        on_delete=models.CASCADE,
        null=True
    )
