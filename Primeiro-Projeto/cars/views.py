from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Car

# Create your views here.
def cars_view(request):

    cars = Car.objects.all().order_by('model')    # Sem filtros, trás todos os registros do banco de dados. 
                                                        # OBS: O order_by faz uma ordenação com o campo como parametro, 
                                                            # se passar o - na frente, ele inverte a ordenação
    filtro = request.GET.get('search')  # Buscamos os dados que o usuário está passando pela URL através do search

    #cars = Car.objects.filter(brand__name='Fiat')   # Filtramos pela coluna 'name' na tabela brand (Utilizar 2 underline __)
    #cars = Car.objects.filter(model__contains='Ricardão')   # o atributo 'contains' busca qualquer palavra que contém o filtro passado

    # Diferença entre contains e icontains:
        # o contains busca EXATAMENTE o que o usuário está buscando, levando em consideração maiusculo e minusculo
        # já o icontains faz a busca ignorando maiusculo ou minusculo.

    if filtro:  # Verifica se na variavel 'filtro' contém alguma coisa. Se sim cai no if, se não passa direto.
        cars = Car.objects.filter(model__icontains=filtro)   # Busca pelo modelo que foi passado pela URL
    
    return render(
        request, 
        'pages/cars.html', 
        {'cars': cars }
    )