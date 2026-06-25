from django import forms
from django.core.checks import messages
from django.http import request

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu login'
            }
        ),
    )
    
    senha=forms.CharField(
        label='Senha',
        required=True,
        min_length=6,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            },
            ),
    )
    
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        )
    )
    
    senha_1=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    
    senha_2=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
    )
    
    def clean_nome_cadastro(self):
        
        nome = self.cleaned_data.get("nome_cadastro")
        if ' ' in nome or len(nome) < 3:
            raise forms.ValidationError("Não é possível inserir espaços em branco ou nomes com menos de 3 caracteres.")
        else:
            return nome
        
    # if form["senha_1"].value() != form["senha_2"].value():
    #     messages.error(request, 'As senhas não coincidem.')
    #     return redirect('register')
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")
        
        if senha_1 and senha_2 and senha_1 != senha_2:
            raise forms.ValidationError("As senhas não coincidem.")
        else:
            return senha_2
                    