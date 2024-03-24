carros = [] # Criamos uma lista

carros.append('Marea') # O 'append' adiciona elementos a lista. OBS: O elemento sempre será adicionado ao final da lista
print(carros)
carros.append('Fusca')
print(carros)
carros.append(10)
print(carros)

print('------------------------')

lista_carros = ['Marea', 'Fusca', 10]   # Podemos passar diretamente os valores também
print(lista_carros)
lista_carros.append('Kombi')
print(lista_carros)
lista_carros.insert(1, 'Corsa') # O 'insert' serve para inserir elementos em posições específicas. Ele usa dois parâmetros, a posição e o valor que desejamos criar
print(lista_carros)

print('------------------------')

# Remover elementos
print(lista_carros)
lista_carros.pop()  # O elemento 'pop' remover sempre o último elemento da minha lista
print(lista_carros)
del lista_carros[0]  # Remove elementos através do indice
print(lista_carros)
lista_carros.remove('Fusca') # Remove o elemento através do valor
print(lista_carros)

print('------------------------')

qts_carros = ['Fusca', 'Fusca', 'Kombi', 'Marea']
print(qts_carros.count('Fusca'))    # O count conta quantos elementos existem através do valor
qts_carros.append('Fusca')
print(qts_carros.count('Fusca'))
del qts_carros[0]
print(qts_carros.count('Fusca'))

print('------------------------')

# Inverter posições
print(qts_carros)
qts_carros.reverse()    # Inverte as posições da lista
print(qts_carros)

print('------------------------')

qts_carros.sort()   # O 'sort' organiza os elementos em ordem 
print(qts_carros)

numero = [2, 1, 8, 9, 7, 5]
numero.sort()
print(numero)