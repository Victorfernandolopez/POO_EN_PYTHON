#clase padre
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("hola estoy hablando un poco")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        print(f"mi habilidad es: {self.habilidad}")

# herencia multiple: Heredamos de 2 clases diferentes propiedades y métodos
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
roberto = EmpleadoArtista("Roberto", 35, "Español", "Pintura", 5000, "La Nueva Imagen y Imagen")

#como saber si empleado es una subclase de artista
herencia = issubclass(EmpleadoArtista, Artista)
#mostrar resultado
print(f"La clase EmpleadoArtista es una subclase de Artista: {herencia}")

#como saber si un objeto es una instancia de una clase

isinstance = isinstance(roberto, EmpleadoArtista)


