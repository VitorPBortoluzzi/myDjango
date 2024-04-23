from django import forms
from django.db import models

class BuscaUsuarioForm(forms.Form):    
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_USUARIOS = (
        (None, '-----'),
        ('ADMINISTRADOR', 'Administrador'),
        ('ENFERMEIRO', 'Enfermeiro' ),
        ('MÉDICO', 'Médico' ),
        ('TÉCNICO', 'Técnico' ),
    )

    tipo = forms.ChoiceField(label='Tipo de Usuarios', choices=TIPOS_USUARIOS, required=False)
    nome = forms.CharField(label='Nome', max_length=100, required=False)