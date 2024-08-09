class Celular:
    
    # Constructor de la clase Celular
    def __init__(self, marca, modelo, camara):
        #propiedades del objeto
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

#instanciando un objeto de la clase Celular

mi_celular = Celular("Samsung", "Galaxy S21 Ultra", "12MP")

#accediendo a las propiedades del objeto

print(mi_celular.marca)
print(mi_celular.modelo)
print(mi_celular.camara)

#modificando las propiedades del objeto

mi_celular.marca = "Huawei"
mi_celular.modelo = "P30 Pro"
mi_celular.camara = "10MP"
