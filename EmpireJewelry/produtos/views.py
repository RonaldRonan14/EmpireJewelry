from django.shortcuts import render, redirect
from django.contrib import messages
from parametros_produtos.models import tbl_tipo_materiais, tbl_tipo_produtos
from produtos.models import tbl_produtos

def index(request):
    produtos = tbl_produtos.objects.all().order_by('-id')

    return render(request, 'produtos/index.html', {
        'produtos': produtos
    })

def create(request):
    if request.method == 'GET':
        tipo_materiais = tbl_tipo_materiais.objects.all()
        tipo_produtos = tbl_tipo_produtos.objects.all()

        return render(request, 'produtos/create.html', {
            'tipo_materiais': tipo_materiais,
            'tipo_produtos': tipo_produtos
        })
    else:
        novo_produto = tbl_produtos (
            nome_produto = request.POST['nomeProduto'],
            descricao_produto = request.POST['descricaoProduto'],
            tipo_produto = tbl_tipo_produtos.objects.get(id = request.POST['tipoProduto']),
            tipo_material = tbl_tipo_materiais.objects.get(id = request.POST['tipoMaterial'])
        )

        novo_produto.save()

        messages.success(request, 'Cadastrado com sucesso')

        return redirect('/produtos')
    
def edit(request, id_produto):
    if request.method == 'GET':
        produto = tbl_produtos.objects.get(id = id_produto)
        tipo_materiais = tbl_tipo_materiais.objects.all()    
        tipo_produtos = tbl_tipo_produtos.objects.all()
        return render(request, 'produtos/edit.html', {
            'produto': produto,
            'tipo_materiais': tipo_materiais,
            'tipo_produtos': tipo_produtos
        })
    else:
        produto = tbl_produtos.objects.get(id = id_produto)
        produto.nome_produto = request.POST['nomeProduto']
        produto.descricao_produto = request.POST['descricaoProduto']
        produto.tipo_produto = tbl_tipo_produtos.objects.get(id = request.POST['tipoProduto'])
        produto.tipo_material = tbl_tipo_materiais.objects.get(id = request.POST['tipoMaterial'])

        produto.save()

        messages.success(request, f'Produto do id {id_produto} modificado com sucesso com sucesso')

        return redirect('/produtos')

def delete(request, id_produto):
    if request.method == 'GET':
        produto = tbl_produtos.objects.get(id = id_produto)
        return render(request, 'produtos/delete.html', { 'produto': produto })
    else:
        produto = tbl_produtos.objects.get(id = id_produto)
        produto.delete()

        messages.success(request, 'Produto deletado com sucesso')

        return redirect('/produtos')