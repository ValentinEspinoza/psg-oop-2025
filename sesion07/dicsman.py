	# Definición
class Pato:
    sonido = "cuac"
    def emitir_sonido(self):
        print (f"El pato 🦆 hace: {self.sonido}")
 
class Gato:
    sonido = "miau"
    def emitir_sonido(self):
        print (f"El gato 🐱 hace: {self.sonido}")

class Campana:
    sonido = "ding"
    def emitir_sonido(self):
        print (f"La campana 🔔 hace: {self.sonido}")
 
class Tambor:
    sonido = "boom"
    def emitir_sonido(self):
        print (f"El tambor 🥁 hace: {self.sonido}")
 
class Discman:
    def reproducir_sonido(self, objeto):
        objeto.emitir_sonido()


# Uso
pato = Pato()
gato = Gato()

discman = Discman()

discman.reproducir_sonido(pato)
discman.reproducir_sonido(gato)

campana = Campana()
tambor = Tambor()
discman.reproducir_sonido(campana)
discman.reproducir_sonido(tambor)