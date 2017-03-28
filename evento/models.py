from django.db import models
from django.utils import timezone




class Evento(models.Model):
    nome = models.CharField('nome', max_length=200, null = False)
    eventoPrincipal = models.CharField('eventoPrincipal', max_length=200, null = True)
    sigla = models.CharField('sigla', max_length=200, null = True)
    dataEHoraDeInicio = models.DateTimeField('data e hora de início', null = True)
    palavrasChave = models.CharField('palavras chave', max_length=600, null = True)
    logotipo = models.CharField('logotipo', max_length=600, null = True)
    #realizador
    cidade = models.CharField('cidade', max_length=60, null = True)
    uf =  models.CharField('uf', max_length=2, null = True)
    endereco = models.CharField('endereco', max_length=600, null = True)
    cep = models.CharField('palavras chave', max_length=50, null = True)

    
    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()


        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)

