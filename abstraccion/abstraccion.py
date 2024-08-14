class Auto:
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("El auto se ha encendido")
    
    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print("conduciendo...")

mi_auto = Auto()

mi_auto.conducir()

#explicacion de porque hay abstraccion en este codigo

#El estado del auto se encapsula en una variable privada, _estado. Esto significa que esta variable solo puede ser accedida y modificada dentro de la clase Auto. Esto evita que el estado del auto sea modificado de manera externa a la clase y asegura que solo los métodos propios de la clase Auto puedan manipular este estado.  En cambio, la variable estado es pública y puede ser accedida desde fuera de la clase. Esto hace que sea más fácil de utilizar y manejar el estado del auto. Además, el método conducir() puede verificar el estado del auto antes de con dolarlo, evitando que se ejecute el método encender() si el auto está apagado. Esto también es una forma de abstracción en el código, ya que la condicion de encendido está encapsulada en el método conducir(). 