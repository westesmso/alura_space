from django.shortcuts import render, redirect

from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User
from django.contrib import auth, messages 

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome_login = form["nome_login"].value()
            senha = form["senha"].value()
            usuario = auth.authenticate(
                request,
                username=nome_login,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'Login realizado com sucesso, {nome_login}!')
                return redirect('index')
            else:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
                return redirect('login')
            
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
           
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe.')
                return redirect('register')
           
            try: 
                usuario = User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha
                )
                usuario.save()
                messages.success(request, f'Usuário {nome} cadastrado com sucesso!')
                print(f'Usuário {nome} cadastrado com sucesso!')
                return redirect('login')
                
            except Exception as e:
                    messages.error(request, f'Erro ao cadastrar usuário: {str(e)}')
                    print(f'Erro ao cadastrar usuário: {str(e)}')
                    return redirect('register')
    
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('index')