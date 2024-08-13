#que hace un decorador en Python?
#Un decorador en Python es una función que toma otra función como argumento, la modifica o extiende, y la devuelve como resultado.
#Los decoradores se utilizan para agregar funcionalidad a las funciones sin alterar su código original.
#Un ejemplo de decorador en Python es el devolver el resultado de una función en mayúsculas.
#o para hacer validar la entrada de una función antes de ejecutarla.


def decorador(funcion):
    def funcion_decorada():
        print("antes de llamar a la funcion")
        funcion()
        print("despues de llamar a la funcion")
    return funcion_decorada()

# def saludo():
#     print("Hola, mundo!")

# # Decorando la función saludo con el decorador decorador
# decorador(saludo) 

@decorador
def saludo():
    print("Hola, mundo!")

saludo() # Imprime: antes de llamar a la funcion, despues de llamar a la funcion, Hola, mundo!