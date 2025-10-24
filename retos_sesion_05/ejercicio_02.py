# clase padre 
class Nadador:
    def nadar(self):
        print("Estoy nadando en el agua")

# clase padre 
class Volador:
    def volar(self):
        print("Estoy volando por el aire")

# Clase pez: hereda de Nadador
class Pez(Nadador):
    def mostrar(self):
        print("Soy un Pez y puedo nadar")

# Clase pajaro: hereda de Volador
class Pajaro(Volador):
    def mostrar(self):
        print("Soy un Pájaro y puedo volar")

# Clase pato: hereda de Nadador y Volador
class Pato(Nadador, Volador):
    def mostrar(self):
        print("Soy un Pato y puedo nadar y volar")


# Uso
pez = Pez()
pez.mostrar()
pez.nadar()

pajaro = Pajaro()
pajaro.mostrar()
pajaro.volar()

pato = Pato()
pato.mostrar()
pato.nadar()
pato.volar()
