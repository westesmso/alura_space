from django import forms

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
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu email'
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
                'class': 'form-control col-6 col-lg-6',
                'placeholder': 'Digite sua senha'
            },
            ),
    )
    
    confirmacao_senha=forms.CharField(
        label='Confirmação de Senha',
        required=True,
        min_length=6,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control col-6 col-lg-6',
                'placeholder': 'Digite sua senha'
            },
            ),
    )