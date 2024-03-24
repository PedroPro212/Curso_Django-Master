meu_dicio = {'nome': 'Pedro', 'idade': 20, 'profissão': 'Dev'}  # Dicionários começam com {} e listas com []
print(meu_dicio)

print('------------------------')

print(meu_dicio['nome'])    # Para acessar a chave do dicionário
print(meu_dicio['profissão'])

print('------------------------')

print(meu_dicio.get('nome '))   # Passa o nome da chave

print('------------------------')

meu_dicio.pop('idade')   # Remove elementos de dentro do dicionários
print(meu_dicio)

print('------------------------')

meu_dicio = {'nome': 'Pedro', 'idade': 20, 'profissão': 'Dev'}
print(meu_dicio.keys())     # Mostra todas as chaves

print('------------------------')

print(meu_dicio.values())   # Mostra todos os valores

print('------------------------')

print(meu_dicio.clear())    # Limpa todo o dicionário

print('------------------------')

pessoa = {
    'nome': 'Felipe',
    'idade': '19',
    'profissão': 'Dev',
    'interesses': ['Python', 'PHP', 'Javascript'],
    'pet': {
        'nome': 'Loki',
        'idade': '1',
        'peso': '2kg'
    }
}

print(pessoa.get('nome'))
print(pessoa.get('interesses'))     # Irá trazer uma lista
print(pessoa.get('interesses')[2])  # Retorna a posição do interesse da pessoa
print(pessoa.get('pet'))
print(pessoa.get('pet').get('nome'))
print(pessoa['pet']['peso'])
print(pessoa['pet'].get('idade'))

print('------------------------')

pessoa  # Cria novamente a lista

pessoa['ano_nascimento'] = 2004     # Adiciona um elemento a lista
pessoa['cores_favoritas'] = ['azul', 'branco', 'verde']     # Adicionamos uma lista
pessoa['mae'] = {       # Adcionamos um dicionário dentro do dicionário
    'nome': 'Leila',
    'idade': 37
}
print(pessoa)