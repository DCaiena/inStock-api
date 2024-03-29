from django.db import models

# Create your models here.


class Lote(models.Model):
    nome_produto = models.CharField(max_length=100, unique=True)
    quantidade = models.IntegerField(null=True, blank=True)
    codigo = models.IntegerField(unique=True)
    fabricacao = models.DateField()
    validade = models.DateField()
    entrada = models.DateField()

    def __str__(self):
        return self.nome_produto


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    codigo = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=150)
    lote = models.ForeignKey(Lote, models.DO_NOTHING)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        #adicionando o código do lote ao produto
        self.codigo = self.lote.codigo
        # Call the real save() method
        super(Produto, self).save(*args, **kwargs)
