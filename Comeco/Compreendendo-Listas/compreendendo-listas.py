# Exemplo 1 de fazer
numeros = [1, 2, 3, 4, 5]   # Criamos uma lista
print(numeros)

numeros_dobrados = []   # Criamos uma lista vazia

for numero in numeros:  # Percorre a lista de números
    numeros_dobrados.append(numero * 2) # Para cada número da lista números, multiplica por 2 e adiciona a lista 'numeros_dobrados'

print(numeros_dobrados)

print('------------------------')

# Exemplo 2 de fazer
numeros = [1, 2, 3, 4, 5]   # Criamos uma lista
print(numeros)

numeros_dobrados = [numero * 2 for numero in numeros]   # Compresão de lista
print(numeros_dobrados)

print('------------------------')

nomes = ['Ana', 'Pedro', 'Felipe', 'Carlos', 'Arlindo']
print(nomes)

nomes_caps = []

# Modo 1
for nome in nomes:
    nomes_caps.append(nome.upper())
print(nomes_caps)

# Modo 2
nomes_mais = [nome.upper() for nome in nomes]
print(nomes_mais)

print('------------------------')

nomes_A = [nome.upper() for nome in nomes if nome[0] == 'A']    # Iremos deixar apenas os nomes que começam com a letra A em MAIÚSCULO. O [0] significa a primeira letra. Expressão, for, condição
print(nomes_A)