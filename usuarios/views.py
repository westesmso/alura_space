from django.shortcuts import render

from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    form = CadastroForms()
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    pass