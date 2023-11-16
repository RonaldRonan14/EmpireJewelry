from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from home.models import tbl_bip
from django.contrib import messages
from produtos.models import tbl_produtos

def index(request):
    bip = tbl_bip.objects.all().order_by('-id')
    return render(request, 'home/index.html', { 'bip': bip })

def create(request):
    if request.method == 'GET':
        produtos = tbl_produtos.objects.all()
        data_hora = datetime.now()
        return render(request, 'home/create.html', {
            'produtos': produtos,
            'data_hora': data_hora
        })
    else:
        novo_bip = tbl_bip(
            produto = tbl_produtos.objects.get(id = request.POST['produto']),
            descricao_produto = request.POST['descricaoProduto'],
            data = request.POST['data'],
            hora = request.POST['hora'],
            local = request.POST['local']
        )

        novo_bip.save()

        messages.success(request, 'Cadastrado com sucesso')

        return redirect('/home')
    
def edit(request, id_bip):
    if request.method == 'GET':
        produtos = tbl_produtos.objects.all()
        bip = tbl_bip.objects.get(id = id_bip)
        return render(request, 'home/edit.html', {
            'produtos': produtos,
            'bip': bip
        })
    else:
        bip = tbl_bip.objects.get(id = id_bip)
        bip.produto = tbl_produtos.objects.get(id = request.POST.get('produto'))
        bip.descricao_produto = request.POST['descricaoProduto']
        bip.data = request.POST['data']
        bip.hora = request.POST['hora']
        bip.local = request.POST['local']

        bip.save()

        messages.success(request, f'Registro {id_bip} de bip editado com sucesso')

        return redirect('/home')
    
def delete(request, id_bip):
    if request.method == 'GET':
        bip = tbl_bip.objects.get(id = id_bip)
        return render(request, 'home/delete.html', { 'bip': bip })
    else:
        bip = tbl_bip.objects.get(id = id_bip)
        bip.delete()

        messages.success(request, 'Registro de bip deletado com sucesso')

        return redirect('/home')