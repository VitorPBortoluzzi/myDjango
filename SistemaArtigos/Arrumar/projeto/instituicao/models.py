from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from utils.gerador_hash import gerar_hash

class InstituicaoAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Instituicao(models.Model):
    nome = models.CharField('Nome da Instituição *',  unique= True, db_index=True,max_length=100, help_text='* Campo obrigatório')
    Sigla = models.CharField('Sigla da Instituição *',  max_length=10, null=True, blank =True, help_text='Se houver sigla, por favor, informe.')
    pais = models.CharField('Pais da Instituição *',  max_length=30, help_text='* Campo obrigatório')
    estado = models.CharField('Estado ou Provincia *',  max_length=100)
    cidade = models.CharField('Cidade*',  max_length=100, help_text='* Campo obrigatório')

    is_active = models.BooleanField('Ativo', default=True, help_text='Se ativo, a ativa pode ser usada no sistema')
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)

    objects = models.Manager()
    instituicoes_ativos = InstituicaoAtivoManager()

    
    class Meta:
        ordering            =   ['-is_active','pais','estado','cidade','nome']
        verbose_name        =   'instituição'
        verbose_name_plural =   'instituições'

    def __str__(self):
        if self.sigla:
            return '%s | %s' % (self.nome, self.sigla)
        else:
            return '%s' % (self.nome)

    def save(self, *args, **kwargs):        
        if not self.slug:
            self.slug = gerar_hash()
        if self.sigla:
            self.sigla = self.sigla.upper()
        self.nome = self.nome.upper()
        self.cidade = self.cidade.upper()        
        self.estado = self.estado.upper() 
        self.pais = self.pais.upper() 
        super(Instituicao, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('instituicao_update', kwargs={'slug': self.slug})

    @property
    def get_delete_url(self):
        return reverse('instituicao_delete', kwargs={'slug': self.slug})

