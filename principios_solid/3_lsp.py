#Los objetos de una clase derivada deben poder sustituir a los objetos de la clase base sin alterar el funcionamiento del programa. En otras palabras, las clases derivadas deben ser capaces de cumplir con las expectativas establecidas por la clase base.

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        print("El animal esta volando")

class AveNoVoladora(Ave):
    def volar(self):
        print("El animal no puede volar")

# de esta manera las clases AveVoladora y AveNoVoladora heredan de la clase Ave y pueden inplementar todo lo de la clase Ave, pero con sus propias versiones de la función volar.

#ejemplo de lo que estaria mal:
class Ave:
    def volar(self):
        print("El animal esta volando")

class pinguino(Ave):
    def volar(self):
        print("El pinguino no esta volando")

def hacer_volar(ave = Ave):
    return ave.volar()

print(hacer_volar(pinguino())) # Esto imprimiría "El pinguino no esta volando", pero se debería imprimir "El animal esta volando" ))
#no cumple con el principio de sustitución porque pinguino no puede volar como si esta dispuesto en la clase base Ave.