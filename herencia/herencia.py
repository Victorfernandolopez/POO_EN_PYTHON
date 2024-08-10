#herencia: Python utiliza una técnica llamada herencia para permitir la creación de clases derivadas de otras clases. Una clase derivada hereda todos los atributos y métodos de su clase base.

class A:
    def hablar(self):
        print("hola desde la clase A")

class F:
    def hablar(self):
        print("hola desde la clase F")

class B(A):
    def hablar(self):
        print("hola desde la clase B")

class C(F):
    def hablar(self):
        print("hola desde la clase C")

class D(B, C):
    def hablar(self):
        print("hola desde la clase D")

d = D()
d.hablar()  # imprime: hola desde la clase D
A.hablar(d)  # imprime: hola desde la clase A
F.hablar(d)  # imprime: hola desde la clase F
B.hablar(d)  # imprime: hola desde la clase B
C.hablar(d)  # imprime: hola desde la clase C

#La herencia permite mantener el código DRY (Don't Repeat Yourself) y simplificar el código de las clases derivadas.

#Ejemplo:
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        print(f"{self.nombre} come")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} ladra")

class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} maulla")

perro = Perro("Buddy")
perro.comer()  # imprime: Buddy come
perro.ladrar()  # imprime: Buddy ladra
gato = Gato("Miau")
gato.comer()  # imprime: Miau come
gato.maullar()  # imprime: Miau maulla

#La herencia múltiple puede ser útil cuando se necesita manejar la herencia en un contexto más complejo.

#Ejemplo:
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} come")

class Mamifero(Animal):
    def lactar(self):
        print(f"{self.nombre} está lactando")

class Perro(Mamifero):
    def ladrar(self):
        print(f"{self.nombre} ladra")

class Gato(Mamifero):
    def maullar(self):
        print(f"{self.nombre} maulla")

perro = Perro("Buddy")
perro.comer()  # imprime: Buddy come
perro.ladrar()  # imprime: Buddy ladra
perro.lactar()  # imprime: Buddy está lactando
gato = Gato("Miau")
gato.comer()  # imprime: Miau come
gato.maullar()  # imprime: Miau maulla
gato.lactar()  # imprime: Miau está lactando
