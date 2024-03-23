a= True
b = False

if a and b:
    print('Atendeu a condição! (and)')
else:
    print('Não atendeu a condição! (and)')

if a or b:
    print('Atendeu a condição! (or)')
else:
    print('Não atendeu a condição! (or)')

print('------------------------')

nome = 'Pedro'
idade = 25
peso = 90

if idade == 25:     # A operação terá que ser igual a 25
    print('Idade correta (==)')
else:
    print('Idade incorreta (==)')

if idade != 25:     # A operação terá que ser diferente de 25
    print('Idade correta (!=)')
else:
    print('Idade incorreta (!=)')

print('------------------------')

if nome == 'Pedro' and idade == 24:     # Caso nome for verdadeiro e idade falsa
    print("Dados incorretos! (and)")
else:
    print("Dados incorretos! (and)")

if nome == 'Pedro' or idade == 24:
    print("Dados incorretos! (or)")
else:
    print("Dados incorretos! (or)")

print('------------------------')

if (nome == 'Pedro' or idade == 25) and peso == 90:     # Mais de um operador
    print("Dados incorretos!")
else:
    print("Dados incorretos!")