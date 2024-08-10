#clase padre
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("hola estoy hablando un poco")

#herencia simple: empleado hereda de persona
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo, salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

#herencia jerarquica: empleado y estudiante heredan de persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad

#herencia multiple: PersonaNormal hereda de persona(clase padre) y de estudiante
class PersonaNormal(Persona,Estudiante):
    pass


roberto = Empleado("Roberto",43,"Argentino","programador", 100000)

roberto.hablar()
