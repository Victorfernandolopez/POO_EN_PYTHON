class Celular:
    
    # Constructor de la clase Celular
    def __init__(self, marca, modelo, camara):
        #propiedades del objeto
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #todas las funciones que se crean dentro de una clase se denominan métodos
    
    def llamar(self):
        print(f"estas haciendo una llamada desde {self.modelo}")
    
    def cortar_llamada(self):
        return "Cortando llamada..."

Celular = Celular("Samsung", "Galaxy S21", "12 MP")

Celular.llamar()