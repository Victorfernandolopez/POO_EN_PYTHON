"""
crear una clase estudiante que tenga los atributos nombre, edad, grado.
ademas hay que agregar un metodo que se llame estudiar y agregar el mensaje "el estudiante (nombre) esta estudiando".
crear una instancia usando el metodo, pero para esto habria que generar una interaccion con el usuario. se tiene que pedir el nombre,edad y grado y acontinuacion instanciar esta clase y mostrar los datos de la clase creada.
si despues de registrado el estudiante el usuario escribe "estudiar", utilizar el metodo estudiar() no case sensitive
"""

class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def Estudiar(self):
        print(f"el estudiante {self.nombre} esta estudiando")


#interaccion con el usuario
nombre = input("ingrese su nombre: ").lower()
edad = input("ingrese su edad: ").lower()
grado = input("ingrese su grado: ").lower()

#instanciar clase
<<<<<<< HEAD
estudiante1 = Estudiante(nombre,edad,grado)
=======
estudiante1 =Estudiante(nombre,edad,grado)
>>>>>>> 388a1a45b51b0a93d2afa644e062042d2ce88f91

#mostrar datos de la clase creada
print(f"nombre: {estudiante1.nombre}")
print(f"nombre: {estudiante1.edad}")
print(f"nombre: {estudiante1.grado}")

#ver si el usuario utiliza la palabra "estudiar"
palabra = input("ingrese una palabra: ").lower()

if palabra == "estudiar":
    estudiante1.Estudiar()