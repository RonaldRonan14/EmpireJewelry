from django.contrib import admin
from .models import tbl_tipo_materiais, tbl_tipo_produtos

admin.site.register([
    tbl_tipo_produtos,
    tbl_tipo_materiais
])