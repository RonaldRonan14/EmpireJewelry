from django.db import models
from parametros_produtos.models import tbl_tipo_materiais, tbl_tipo_produtos

class tbl_produtos(models.Model):
    nome_produto = models.CharField(max_length=150, null=False)
    descricao_produto = models.CharField(max_length=254, null=False)
    tipo_produto = models.ForeignKey(tbl_tipo_produtos, on_delete=models.PROTECT, null=False)
    tipo_material = models.ForeignKey(tbl_tipo_materiais, on_delete=models.PROTECT, null=False)