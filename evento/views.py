from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import *


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                </ul>
            """
    return HttpResponse(html)




def listaEventos(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                </ul>
            """"<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    for evento in lista:
        html += '<li>Nome: {}	      Data e Hora Início:  {}'"<a href='/evento/{}'>     Ver detalhe</a></li>".format(evento.nome,  evento.dataEHoraDeInicio, evento.id)
    return HttpResponse(html)



def pesqEvento(request, pk):
	html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                </ul>
            """"<h1>Detalhamento do Evento</h1>"
	evento = Evento.objects.get(pk=pk)
	html += '<h2>Nome: {} </h2>'.format(evento.nome)
	html += 'Data e Hora de Início: {}'.format(evento.dataEHoraDeInicio)
	html += 'Evento Principal: {} <br>'.format(evento.eventoPrincipal)
	html += 'Sigla: {} <br>'.format(evento.sigla)
	html += 'Palavras-Chave: {} <br>'.format(evento.palavrasChave)
	html += 'Cep: {} <br>'.format(evento.cep)
	html += 'Cidade: {} <br>'.format(evento.cidade)
	html += 'Endereço: {} <br>'.format(evento.endereco)
	html += 'Logotipo: {} <br>'.format(evento.logotipo)
	html += 'UF: {} <br>'.format(evento.uf)






	return HttpResponse (html)





