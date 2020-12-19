import time

### 1) Restaurante:
# Haga una clase llamada Restaurante. El método __init __() para Restaurante
# debe almacenar dos atributos: un restaurant_nombre y un cocina_tipo.

class Restaurante:
    def __init__(self, nombre, tipo):
        self.restaurant_nombre = nombre
        self.cocina_tipo = tipo
        self.numero_servicio = 0

    def describe_restaurant(self):
        return "Restaurante {} y su especialidad {}.".format(self.restaurant_nombre, self.cocina_tipo)
    
    def abrir_restaurant(self, estado):
        self.estado = estado
        if(self.estado == True):
            return "Hemos abierto el restaurant"
        else:
            return "Por hoy hemos cerrado, nos vemos mañana"
    
    def set_numero_servicio(self, numero):
        self.numero_servicio = numero
        return 'Restaurante {}, atendiendo a {} clientes'.format(self.restaurant_nombre, self.numero_servicio)

    def incrementar_numero_servicio(self, incremento):
        self.incremento = incremento
        for b in range(incremento+2):
            print("{} atendiendo a {} clientes".format(
                self.restaurant_nombre, b))
            time.sleep(1)
        print()
        return 'Todos esos clientes atendimos hoy!'


# Cree una instancia llamada restaurante de la clase. Imprima los dos atributos
# individualmente y luego llame a ambos métodos.

a = "----------------------------------------"

print()
restaurante = Restaurante("restaurant", "cocina")
print(restaurante.restaurant_nombre)
print(restaurante.cocina_tipo)
print(restaurante.describe_restaurant())
time.sleep(2)
print('......')
time.sleep(2)
print(restaurante.abrir_restaurant(1))
print()
print(a)
time.sleep(2)

### 2) Tres restaurantes:
# Comience con su clase de la Parte 1. Cree tres instancias diferentes de la
# clase y llame a describe_restaurant() para cada instancia.

Sushi = Restaurante("Ohisushi", "SushiFusión")
Burguer = Restaurante("CaracaBurguer", "Hamburguesas Venezolanas")
Pizza = Restaurante("Milanno's Pizza", "Pizzas familiares")

print(Sushi.describe_restaurant())
print()
print(Burguer.describe_restaurant())
print()
print(Pizza.describe_restaurant())
print()
print(a)
time.sleep(2)

### 3) Número servicio:
# Comience con su programa de la clase Restaurante. Agregue un atributo
# llamado numero_servicio con un valor predeterminado de 0. Cree una
# instancia llamada restaurante de esta clase. Imprima el número de clientes
# que ha atendido el restaurante y luego cambie este valor e imprímalo
# nuevamente.

print()
print(restaurante.restaurant_nombre, 'atendio a',
      restaurante.numero_servicio, 'clientes')
print()
time.sleep(1)

# Agregue un método llamado set_numero_servicio() que le permita establecer
# el número de clientes que han sido atendidos. Llame a este método con un
# nuevo número e imprima el valor nuevamente.

setattr(restaurante, 'numero_servicio', 8)
print(restaurante.restaurant_nombre, 'atendio a',
      restaurante.numero_servicio, 'clientes')
print()
print(a)
time.sleep(2)

# Agregue un método llamado incrementar_numero_servicio() que le permite
# incrementar la cantidad de clientes que han recibido servicios. 

print()
restaurante = Restaurante("restaurant", "cocina")
print(restaurante.restaurant_nombre)
print(restaurante.cocina_tipo)
print(restaurante.describe_restaurant())
time.sleep(2)
print('......')
time.sleep(2)
print(restaurante.abrir_restaurant(1))
print()
print(a)
time.sleep(2)

# Llame a este método con el número que desee y que pueda representar 
# cuántos clientes se atendieron, digamos, en un día de trabajo.

print()
print(restaurante.set_numero_servicio(0))
time.sleep(0.5)
print(restaurante.set_numero_servicio(5))
time.sleep(0.5)
print(restaurante.set_numero_servicio(12))
print()
print(a)
time.sleep(2)  
print(restaurante.incrementar_numero_servicio(10))
print(restaurante.abrir_restaurant(0))
print(a)
