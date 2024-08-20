#principio de abierto/cerrado

#El software debe estar abierto para la extensión, pero cerrado para la modificación. Esto significa que el comportamiento de una clase debe poder extenderse sin modificar su código fuente, generalmente mediante la herencia o la implementación de interfaces.

#Ejemplo:
class Notificador(self):
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError("Debe implementar el método notificar")
#el método notificar es una operación que debe ser implementada en las clases que herede de Notificador
#raise: NotImplementedError genera una excepción cuando se intenta instanciar una clase que no implementa un método abstracto

class NotificacionEmail(Notificador):
    def notificar(self):
        print(f"Notificación enviada a {self.usuario.email}")

class NotificacionSMS(Notificador):
    def notificar(self):
        print(f"Notificación enviada al número {self.usuario.telefono}")

#En este caso, si se quiere agregar una nueva forma de notificación, solo se necesita crear una nueva clase que herede de Notificador y implemente el método notificar. Esto garantiza que el código sea flexible y extensible.