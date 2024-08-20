#principi de responsabilidad unica
#una clase solo debe tener una responsabilidad

#ejemplo de mala práctica

class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto

    def calcular_salario(self):
        if self.puesto == "Gerente":
            return 5000
        elif self.puesto == "Jefe de proyecto":
            return 3000
        elif self.puesto == "Desarrollador":
            return 2000
        else:
            return 0
#explicación: Esta clase tiene tres responsabilidades: calcular salario, obtener nombre y obtener puesto. Esto puede generar problemas si se quiere agregar más funcionalidades en el futuro.


#ejemplo de buena práctica
class Empleado:
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
        self.salario_calculador = SalarioCalculador()

    def calcular_salario(self):
        return self.salario_calculador.calcular_salario(self.puesto)

class SalarioCalculador:
    def calcular_salario(self, puesto):
        if puesto == "Gerente":
            return 5000
        elif puesto == "Jefe de proyecto":
            return 3000
        elif puesto == "Desarrollador":
            return 2000
        else:
            return 0

#explicación: Ahora la clase Empleado solo tiene una responsabilidad: calcular salario, y la clase SalarioCalculador tiene una responsabilidad: calcular salario por puesto. Esto facilita el mantenimiento y el agregado de nuevas funcionalidades en el futuro.
