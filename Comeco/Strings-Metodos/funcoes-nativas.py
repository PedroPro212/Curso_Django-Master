texto = 'AULA PYCODEBR'

print(len(texto))   # Retorna o tamanho do texto

print('------------------------')

print(texto.count('A')) # Retorna quantas ocorrências do caracter ele encontrou dentro da variavel
print(texto.count('AULA'))

print('------------------------')

print(texto.find('AULA'))   # Retorna a posição que esse trecho começa na string
print(texto.find('PYCODEBR'))   # Encontrou o texto apartir da posição/caracter 5 

print('------------------------')

print(texto.upper())    # Transforma todo o texto em MAIÚSCULO
print(texto.lower())    # Transforma todo o texto em MINÚSCULO
print(texto.capitalize())   # Coloca a primeira letra da string em maiúsculo
print(texto.title())    # Transforma a primeira letra de todas as frase em maiúsculo

print('------------------------')

print(texto.split())    # Retorna e divide em uma lista com todas as palavras que ele encontrou 

lista_palavras = texto.split() 
texto_unido = '-'.join(lista_palavras)     # O join junta todas essas listas de palavras e coloca um separador que quisermos
print(texto_unido)

texto_espaco = '    AULA PYCODEBR   '
print(texto.strip())    # Remove os espaços em brancos/vazios
print(texto_espaco.rstrip())    # Remove os espaços em branco da direira
print(texto_espaco.lstrip())    # Remove os espaços em brancos da esquerda