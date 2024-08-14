#importar la libreria ABC (Abstract Base Classes)

from abc import ABC, abstractmethod

#crear una clase abstracta llamada Persona que hereda de ABC

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    @abstractmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# dalton = Persona("Dalton", 30, "masculino", "developer") # esta linea de codigo generara un error porque la clase Persona es abstracta, no se puede instanciar.

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    def hacer_actividad(self):
        print(f"{self.nombre} está haciendo {self.actividad}.")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    def hacer_actividad(self):
        print(f"acualmente {self.nombre} está {self.actividad}.")

victor = Estudiante("Victor", 25, "masculino", "developer")
victor.presentarse()
victor.hacer_actividad()

trabajador = Trabajador("Juan", 40, "masculino", "developer en una empresa")
trabajador.presentarse()
trabajador.hacer_actividad()