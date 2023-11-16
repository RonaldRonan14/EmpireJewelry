from django.db import models

class tbl_tipo_produtos(models.Model):
    nome_tipo_produto = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nome_tipo_produto

class tbl_tipo_materiais(models.Model):
    nome_tipo_material = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nome_tipo_material