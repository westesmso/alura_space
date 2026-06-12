from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha1"].value() != form["senha2"].value():
                return redirect('register')
            
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha1"].value()
            
            if User.objects.filter(username=nome).exists():
                return redirect('register')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')
    
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    pass