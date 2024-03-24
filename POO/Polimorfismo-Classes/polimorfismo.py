class Animal:   # Criei uma classe principal

    def emitir_som(self):
        print("Qualquer som")

class Cachorro(Animal):

    def emitir_som(self):   # Sobreescrevo uma função da classe herdada
        print('Au au!')

class Gato(Animal):

    def emitir_som(self):
        print('Miau!')


cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()