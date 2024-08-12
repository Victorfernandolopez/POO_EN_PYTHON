"""
Crear un sstema para una escuela. vamos a tener dos clases principales:
persona y estudiante. la clase persona tendra los atributos de nombre y edad y un metodo que imprima el nombre y la edad de la  persona. la clase estudiante heredara de la clase persona y tambien tendra un atributo adicional: grado y un metodo que imprima el grado del estudiante.
deberas utilizar supe en el metodo de init para reutilizar el codigo de la clase padre (persona).. luego crea una instancia de la clase estudiante e imprime sus atributos y utiliza sus metodos para asegurarte de que todo funciona correctamente.
"""
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrarDatos(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")   

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado=grado
    
    def mostrarGrado(self):
        print(f"grado: {self.grado}")

estudiante = Estudiante("juan","24","10mo")
estudiante.mostrarDatos()
estudiante.mostrarGrado()

#----------------------------------------------------------------------


"""
imagina que estas modelando animales en un zoologico. crear tres clases: "animal", "mamifero" y "ave". la clase animal debe tener un metodo llamado "comer" . la clase "mamifero" debe tener un metodo llamado "amamantar" y la clase ave un metodo llamado "volar".

ahora, crea una clase "murcielago" que herede de mamifero y ave,  en ese orden, y por lo tanto debe ser capaz de amamantar y volar, ademas de comer.

finalmente, juega con el orden de herencia de las clase murcielago y observa como cambia el MRO y el comportamiento de los metodos al usar super()
"""
class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Ave(Animal):
    def Volar(self):
        print("El animal esta volando")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")

class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()

murcielago.comer()
murcielago.Volar()
murcielago.amamantar()

ave = Ave()

ave.Volar()
ave.comer()

#ave.amamantar()  # esto generaria un error porque el objeto ave no hereda el metodo amamantar()