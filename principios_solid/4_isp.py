# principio de segregación de interfaces
#Es mejor tener muchas interfaces específicas para un cliente en particular que una única interfaz general. Esto significa que las clases no deberían depender de métodos que no utilizan, lo que reduce el acoplamiento entre componentes.

from abc import ABC, abstractmethod

# Definimos la interfaz trabajador

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

#definimos la interfaz comedor

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

#definimos la interfaz durmiente

class Dormitorio(ABC):
    @abstractmethod
    def dormir(self):
        pass

# Implementamos las clases que implementan las interfaces
class humano(Trabajador, Comedor, Dormitorio):
    def trabajar(self):
        print("El humano trabaja")
    def comer(self):
        print("El humano come")
    def dormir(self):
        print("El humano duerme")

class robot(Trabajador):
    def trabajar(self):
        print("El robot trabaja")

#forma incorrecta de usar la interfaz

# class trabajador(ABC):
#     @abstractmethod
#     def trabajar(self):
#         pass
#     @abstractmethod
#     def comer(self):
#         pass
#     @abstractmethod
#     def dormir(self):

# class humano(Trabajador):
#     def trabajar(self):
#         print("El humano trabaja")
#     def comer(self):
#         print("El humano come")
#     def dormir(self):
#         print("El humano duerme")

# class robot(Trabajador):
#     def trabajar(self):
#         print("El robot trabaja")

#si ubiesemos implementado la interfaz como la mostrada arriba, no podríamos crear objetos humano y robot de manera independiente, ya que ambas clases heredan de Trababador y deben implementar todos los métodos de la interfaz. inecesariamente deveriamos implementar el metodo comer y dormir a un robot que son cosas que no hacen.