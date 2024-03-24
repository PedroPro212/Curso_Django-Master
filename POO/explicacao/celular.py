class Celular:  # Celular é um objeto
    marca = 'Nokia' # Propriedade
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    def fazer_ligacoes(self):   # Função para fazer ligação
        print("Fazendo ligação..")
    
    def jogar_cobrinha(self):   # Função para jogar cobrinha
        print("Jogando cobrinha...")
    
    def despertador(self):  # Função para o despertador
        print("Despertador...")
    
    def calculadora(self, v1, v2):  # Toda classe tem por obrigação ter o parâmetro self. Self é uma instância da própria classe
        return v1 + v2


celular = Celular()
print(celular.marca)
print(celular.cor)
print(celular.bateria)
print(celular.modelo)
print(celular.tem_camera)

celular.fazer_ligacoes()
celular.jogar_cobrinha()
celular.despertador()
calculado = celular.calculadora(2, 2)   # Passe os dois parâmetros para a função 'calculadora'
print(calculado)