#MRO: MRO (Method Resolution Order) es una lista de clases en la que Python busca el método cuando no encuentra en la clase actual.
# Este orden es importante para la herencia multiple. El primer elemento de la lista es la clase que se va a buscar en primer lugar.
#es el orden en que python busca metodos y atributos entre las clases heredadas.

#Ejemplo de herencia multiple y MRO:
# clase padre A
class A:
    def hablar(self):
        print("hola desde A")

#clase padre F

class F:
    def hablar(self):
        print("hola desde F")

#clase hija B que hereda de A
class B(A):
    def hablar(self):
        print("hola desde B")

#clase hija C que hereda de A
class C(A):
    def hablar(self):
        print("hola desde C")

#clase hija D que hereda de B y C
class D(B, C):
    def hablar(self):
        print("hola desde D")

#clase hija E que hereda de F y D

class E(F, D):
    def hablar(self):
        print("hola desde E")


d = D() # A B C D
d.hablar()
#orden en que va a ir buscando el metodo hablar en el MRO
#mostrar resultado
print(D.mro()) # muestra el MRO de la clase D

#instancia de E que hereda de F y D

e = E()
e.hablar()

#orden en que va a ir buscando el metodo hablar en el MRO
print(E.mro()) # muestra el MRO de la clase E