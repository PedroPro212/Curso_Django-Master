class Forma():

    def area(self):
        pass

class Quadrado(Forma):

    def __init__(self, lado):   # def __init__ é um método construtor da sua classe. Esse método pede para receber um parâmetro inicial
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):

    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2
    

quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)

quadrado = Quadrado(8)
area_quadrado = quadrado.area()
print(area_quadrado)

circulo = Circulo(4)
circulo_calculado = circulo.area()
print(circulo_calculado)