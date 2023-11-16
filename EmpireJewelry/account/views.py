from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def account(request):
    if request.method == 'GET':
        return render(request, 'account/index.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return redirect('/', error = 'Usuário ou senha inválido')
        else:
            login(request, user)
            return redirect('/home')