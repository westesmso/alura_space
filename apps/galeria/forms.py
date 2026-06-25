from django import forms

from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada'],
        labels = {
            'nome': 'Nome da fotografia',
            'legenda': 'Legenda da fotografia',
            'categoria': 'Categoria da fotografia',
            'descricao': 'Descrição da fotografia',
            'foto': 'Arquivo da fotografia',
            'data_fotografia': 'Data da fotografia',
            'usuario': 'Usuário responsável',}
        widgets ={
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da fotografia'
                }
            ),
            'legenda': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Legenda da fotografia'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                },
                choices=Fotografia.OP
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descrição da fotografia'
                }
            ),
            'foto': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'data_fotografia': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'data_fotografia': forms.DateTimeInput(
                format='%d/%m/%Y %H:%M',
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                }
            ),
            'usuario': forms.Select(
                attrs={
                    'class': 'form-control',
                },
                choices=Fotografia._meta.get_field('usuario').related_model.objects.all()
                )
        }