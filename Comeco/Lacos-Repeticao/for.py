def envia_email(cliente):   # Criamos uma função para enviar email que recebe cliente como parâmetro
    print(f'Email enviado para o cliente {cliente}')    # Printa o resultado

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']      # Criamos um array de clientes

for cliente in clientes:    # Criamos um for para percorrer o array de clientes
    envia_email(cliente)    # Chama a função e passa o resultado da repetição como parâmetro

print('------------------------')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']      # Criamos uma lista de clientes

for i ,cliente in enumerate(clientes):    # A função 'enumerate' mostra o indice da lista
    print(i, cliente)    

print('------------------------')

for i in range(10): # A função range retorna uma lista de números, conforme for o número, será repetida n vezes
    print(i)    # Printa o resultado

print('------------------------')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']      # Criamos uma lista de clientes

for i ,cliente in enumerate(clientes):    # A função 'enumerate' mostra o indice da lista
    if i == 2:  # Irá encontrar o indice 2
        break   # Irá PARAR no indice 2       
    envia_email(cliente)    # Irá enviar os emails para a lista até o break

print('------------------------')

clientes = ['Ana', 'Jonas', 'Felipe', 'Cláudio', 'Renato']      # Criamos uma lista de clientes

for i ,cliente in enumerate(clientes):    # A função 'enumerate' mostra o indice da lista
    if i == 2:  # Irá encontrar o indice 2
        continue   # Irá PULAR para o próximo indice     
    envia_email(cliente)    # Irá enviar os emails para a lista até o break