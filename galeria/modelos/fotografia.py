from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    """Representa uma fotografia cadastrada na galeria com seus metadados principais.
    Armazena informações como nome, legenda, categoria, descrição, arquivo e status de publicação.

    Atributos:
        OP: Lista de opções de categoria disponíveis para a fotografia.
        nome: Nome da fotografia exibido na galeria.
        legenda: Legenda curta que acompanha a fotografia.
        categoria: Categoria temática da fotografia baseada nas opções definidas em OP.
        descricao: Descrição detalhada da fotografia.
        foto_nome: Nome do arquivo de imagem associado à fotografia.
        publicada: Indica se a fotografia está visível ou não na galeria.
        data_fotografia: Data e hora em que a fotografia foi registrada ou cadastrada.
    """

    OP = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OP, default='')
    descricao = models.TextField(null=False, blank=False)
    foto_nome = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}, legenda={self.legenda}, categoria={self.categoria}, descricao={self.descricao}, foto_nome={self.foto_nome}, publicada={self.publicada}, data_fotografia={self.data_fotografia}]"
    