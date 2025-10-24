# clase padre
class Vehiculo:
    def __init__(self, medio, velocidad_inicial=0.0):
        self._velocidad = velocidad_inicial   # atributo protegido
        self.medio = medio                    # atributo público

    def get_velocidad(self):
        return self._velocidad

    def set_medio(self, nuevo_medio):
        self.medio = nuevo_medio

    def acelerar(self, cantidad):
        if cantidad > 0:
            self._velocidad += cantidad


# clase hija
class Bicicleta(Vehiculo):
    def __init__(self, medio="terrestre", velocidad_inicial=0.0):
        super().__init__(medio, velocidad_inicial)

    def pedalear(self):
        self.acelerar(5)  # aumenta velocidad en 5


# Clase hija
class Avion(Vehiculo):
    def __init__(self, medio="aéreo", velocidad_inicial=0.0):
        super().__init__(medio, velocidad_inicial)

    def volar(self):
        self.acelerar(300)  # aumenta velocidad en 300


# Ejemplo de uso
bicicleta = Bicicleta()
print("Bicicleta")
print("Medio:", bicicleta.medio)
print("Velocidad inicial:", bicicleta.get_velocidad(), "km/h")
bicicleta.pedalear()
print("Velocidad despues de pedalear:", bicicleta.get_velocidad(), "km/h")

avion = Avion()
print("\nAvión")
print("Medio:", avion.medio)
print("Velocidad inicial:", avion.get_velocidad(), "km/h")
avion.volar()
print("Velocidad despues de volar:", avion.get_velocidad(), "km/h")
