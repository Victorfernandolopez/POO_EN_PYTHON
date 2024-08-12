#que es el polimorfismo 

#metodos con el mismo nombre pero diferentes implementaciones
#se puede llamar a cualquiera de ellos segun el tipo de objeto que se le asigne

#Ejemplo:
class Animal:
    def hablar(self):
        print("El animal esta hablando")
    
class Perro(Animal):
    def hablar(self):
        print("El perro esta ladrando")
    
class Gato(Animal):
    def hablar(self):
        print("El gato esta miau")

#polimorfismo de funciones

def hablar(animal):
    animal.hablar()

perro = Perro()
gato = Gato()

hablar(perro)
#output: El perro esta ladrando
hablar(gato)
#output: El perro esta ladrando

#descripcion del ejercicio: Se define una clase Animal con un metodo hablar(). Luego se crean dos clases Perro y Gato que heredan de Animal y sobreescriben el metodo hablar(). Luego se define una funcion hablar() que recibe un objeto Animal y llama al metodo hablar() de ese objeto. Se crean objetos Perro y Gato y se llama a la funcion hablar() con cada objeto, mostrando el resultado esperado.

#polimorfismo de objetos

print(gato.hablar()) #output: El gato esta miau      o     print(perro.hablar()) #output: El perro esta ladrando

#descripcion del ejercicio: Se muestra que el metodo hablar() de las clases Perro y Gato es llamado segun el tipo de objeto que se le asigne. Se crean objetos Gato y Perro y se imprimen los resultados de llamar al metodo hablar() con cada objeto.

