def qts(texto):     # Criei uma função para ler quantos caracteres possui um texto, essa função recebe o parametro 'texto'
    return str(len(texto))  # Retorna o resultado e converte em string

texto = 'Pedro'    # O usuário digita o texto
textQts = qts(texto)    # Chama a função, passa o parametro para a função qts
print("Quantidade de: " + textQts)  # Mostra para o usuário

print('------------------------')

def somar(a, b):    # Função para somar dois números
    resultado = a + b
    return str(resultado)

print("O resultado é : " + somar(5, 4))

print('------------------------')

def envia_email(nome, email):   # Função para enviar email
    nome_dest = nome
    email_dest = email
    return f'Email enviado para {nome_dest}, dona do email {email_dest}'

pessoas = [     # Criamos um dicionário
    {
        'nome': 'Filipe',   # Onde existe nome
        'email': 'filipe@gmail.com'     # Email da pessoa
    },
    {
        'nome': 'Pedro',
        'email': 'pedro@gmail.com'
    },
    {
        'nome': 'Gabriel',
        'email': 'gabriel@gmail.com'
    }
]

for pessoa in pessoas:  # Criamos um for para percorrer essa lista
    email_enviado = envia_email(pessoa['nome'], pessoa['email'])    # Para cada repetição ele chama a função 'envia_email'
    print(email_enviado)    # Printa o resultado do for