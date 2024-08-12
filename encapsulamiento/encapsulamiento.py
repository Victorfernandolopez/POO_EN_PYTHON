#privado y público en Python
class MiClase:
    def __init__(self):
        self._atributo_privado = "valor_privado"

objeto = MiClase()
print(objeto._atributo_privado) # output: valor_privado

#muy privado en Python
class MiClase2:
    def __init__(self):
        self.__atributo_muyprivado = "valor_privado"

objeto1 = MiClase2()
#print(objeto1.__atributo_muyprivado) # error: name 'MiClase2' has no attribute '__atributo_muyprivado'
# Esto va a fallar porque el atributo no está público y no se puede acceder desde fuera de la clase (como se hace con el atributo privado) 