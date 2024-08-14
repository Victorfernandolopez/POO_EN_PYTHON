import os
os.system("cls")
"""
crear un juego de fusion.
el juego consiste en crear personajes de un juego y que esos personajes se puedan fusionar para formar personajes mas poderosos que tengan mas poder...
para ello deberemos cambiar el comportamiento del operador "+" para que cuando los personajes se fusionen, salga un nuevo personaje con habilidades mejoradas.

una posible formula es: el promedio de las habilidades de ambos, al cuadrado.
"""
# clase Personaje
class Personaje:
    def __init__(self, nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    # mostrar el personaje
    def __str__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad:{self.velocidad})"
    
    #fusionar personaje
    def __add__(self,otro):
        nuevo_personaje = self.nombre + "-" + otro.nombre
        nueva_furza = round(((self.fuerza + otro.fuerza)/2)**1.34)
        nueva_velocidad = round(((self.velocidad + otro.velocidad)/2)**1.34)
        return Personaje(nuevo_personaje,nueva_furza,nueva_velocidad)


#crear personaje 1
goku = Personaje("goku", 100, 100)
print(goku) #sin la funcion str esto mostraria el codigo del objeto

#crear el personaje 2
vegueta = Personaje("Vegueta",99,99)
print(vegueta)

#fusionar los personajes
gogeta = goku + vegueta
print(gogeta)



