from django.db import models
from produtos.models import tbl_produtos

class tbl_bip(models.Model):
    produto = models.ForeignKey(tbl_produtos, on_delete=models.PROTECT, null=False)
    descricao_produto = models.CharField(max_length=254, null=False)
    data = models.DateField(null=True)
    hora = models.TimeField(null=False)
    local = models.CharField(max_length=100, null=False)