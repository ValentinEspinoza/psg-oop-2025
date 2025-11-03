class Pasajero:
    def __init__(self, nombre, destino):
        self.nombre = nombre
        self.destino = destino


class Minibus:
    def __init__(self, numero_ruta, paradas):
        self.numero_ruta = numero_ruta
        self.paradas = paradas
        self.pasajeros = []
        self.indice_parada = 0
        self.sentido = 1  # 1 hacia adelante, -1 hacia atrás

    def parada_actual(self):
        return self.paradas[self.indice_parada]

    def subir_pasajero(self, pasajero):
        if pasajero.destino in self.paradas:
            self.pasajeros.append(pasajero)
            print(f"{pasajero.nombre} sube al minibus. Destino: {pasajero.destino}")
        else:
            print(f"{pasajero.nombre} no puede subir (destino fuera de ruta).")

    def bajar_pasajeros(self):
        bajan = [p for p in self.pasajeros if p.destino == self.parada_actual()]
        for p in bajan:
            print(f"{p.nombre} baja en {self.parada_actual()}.")
        self.pasajeros = [p for p in self.pasajeros if p.destino != self.parada_actual()]

    def avanzar(self):
        self.indice_parada += self.sentido

        # si llega al final de recorrido, invierte sentido
        if self.indice_parada >= len(self.paradas):
            self.indice_parada = len(self.paradas) - 2
            self.sentido = -1
            print("El minibus llego al final y regresa.")
        elif self.indice_parada < 0:
            self.indice_parada = 1
            self.sentido = 1
            print("El minibus llego al inicio y cambia de sentido.")

        print(f"\nParada actual: {self.parada_actual()}")
        self.bajar_pasajeros()

    def mostrar_pasajeros(self):
        if self.pasajeros:
            nombres = [p.nombre for p in self.pasajeros]
            print(f"Pasajeros a bordo: {nombres}")
        else:
            print("No hay pasajeros a bordo.")


# Uso 
# 5 pasajeros 
p1 = Pasajero("Jhon", "Prado")
p2 = Pasajero("Jose", "Perez")
p3 = Pasajero("Carlos", "Arce")
p4 = Pasajero("Luis", "Camacho")
p5 = Pasajero("Juan", "Arce")

# minibus con recorrido circular
minibus = Minibus("Linea A", ["Arce", "Prado", "Perez", "Camacho"])

# punto de partida
print(f"\nInicio en {minibus.parada_actual()}")

# suben pasajeros
minibus.subir_pasajero(p1)
minibus.subir_pasajero(p2)
minibus.subir_pasajero(p3)

minibus.mostrar_pasajeros()

# avanza al Prado
minibus.avanzar()
minibus.mostrar_pasajeros()

# en Prado
minibus.subir_pasajero(p4)

# avanza a Perez
minibus.avanzar()
minibus.mostrar_pasajeros()

# en Perez
minibus.subir_pasajero(p5)

# avanza a Camacho 
minibus.avanzar()
minibus.mostrar_pasajeros()

# el minibus llega al final y regresa
minibus.avanzar()  # Perez
minibus.mostrar_pasajeros()

minibus.avanzar()  # Prado
minibus.mostrar_pasajeros()

minibus.avanzar()  # Arce
minibus.mostrar_pasajeros()
