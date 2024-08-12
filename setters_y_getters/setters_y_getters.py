#getter
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
        
    def get_edad(self):
        return self._edad
        
    def set_nombre(self, nombre):
        self._nombre = nombre
        
    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
        else:
            print("La edad no puede ser negativa")

#ejemplo obtener nombre y edad

persona = Persona("Juan", 25)
print(persona.get_nombre())
print(persona.get_edad())

#setter
#ejemplo cambiar nombre y edad

persona.set_nombre("Pedro")
persona.set_edad(30)
print(persona.get_nombre())
print(persona.get_edad())