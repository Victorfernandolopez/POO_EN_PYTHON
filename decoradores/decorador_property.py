class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre


victor = Persona("Victor", 25)
nombre = victor.nombre
print(nombre) # output: Victor

victor.nombre = "Vicente"
nombre = victor.nombre
print(nombre) # output: Vicente
