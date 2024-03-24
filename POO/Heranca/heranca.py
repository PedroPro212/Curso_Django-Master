class Carro:    # Criamos uma classe Carro
    numero_rodas = 4
    qts_passageiros = 5

    def acelerar(self):
        print('Acelerando..')

    def frear(self):
        print('Freando...')
    
    def buzinar(self):
        print('Buzinando...')

class Uno(Carro):   # A class Uno herda os elementos da classe Carro
    modelo = 'Uno'
    marca = 'Fiat'
    ano = 1992

uno = Uno()
uno.acelerar()
print(uno.numero_rodas)