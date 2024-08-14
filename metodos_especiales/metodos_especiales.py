import os
os.system("cls")

class Persona:
    #metodo especial __init__ se ejecuta cuando se crea un objeto de la clase Persona 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #metodo especial __str__ se ejecuta cuando se imprime un objeto de la clase y hace referencia al objeto, lo que se muestra en la consola o terminal del programa 
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def __add__(self, other):
        return Persona(self.nombre + " " + other.nombre, self.edad + other.edad)

#creando objetos

persona1 = Persona("Juan", 25)
persona2 = Persona("Ana", 30)

#imprimiendo objetos

print(persona1)
print(persona2)

#sumando objetos

persona3 = persona1 + persona2
print(persona3)

