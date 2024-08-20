#principio de invercion de independencias

from abc import ABC, abstractmethod
class VerficadorOrtografico(ABC):
    @abstractmethod
    def verificar_ortografia(self, palabra):
        pass

class Diccionario(VerficadorOrtografico):
    def verificar_ortografia(self, palabra):
        #logica para verificar la ortografia en un diccionario
        pass

class correctorOrtografico:
    def __init__(self, verificador):
        self.verificador = verificador
    
    def corregir_ortografia(self, texto):
        #usamos el verificador para corregir la ortografia

#en este ejemplo, la clase correctorOrtografico no depende de la clase Diccionario, sino que se inyecta como dependencia un objeto de la clase VerficadorOrtografico. Esto hace que la clase correctorOrtografico sea independiente de la implementación del verificador, lo que facilita su reutilización y mantenimiento.