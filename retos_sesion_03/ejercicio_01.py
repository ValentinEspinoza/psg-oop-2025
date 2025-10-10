class Atleta:
    max_energia = 100
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 80   # valor inicial
        self.fuerza = 10    # valor inicial

    def entrenar(self):
        if self.energia > 10:
            self.fuerza += 5
            self.energia -= 10
            print(f"{self.nombre} entrenó. 💪 Fuerza: {self.fuerza}, Energía: {self.energia}")
        else:
            print(f"{self.nombre} está muy cansado para entrenar 😴")

    def descansar(self):
        self.energia += 20
        if self.energia > Atleta.max_energia:
            self.energia = Atleta.max_energia
        print(f"{self.nombre} descansó. 😌 Energía: {self.energia}")

    def comer(self):
        self.energia += 15
        if self.energia > Atleta.max_energia:
            self.energia = Atleta.max_energia
        print(f"{self.nombre} comió una hamburguesa 🍔. Energía: {self.energia}")

    
    @classmethod
    def incremento_fuerza_energia(cls, nueva_fuerza_entrenar, nueva_energia_descanso):
        cls.fuerza = nueva_fuerza_entrenar
        cls.energia = nueva_energia_descanso
        print(f"Cambios aplicados: fuerza por entrenar = +{cls.fuerza}, "
              f"energía por descansar = +{cls.energia}")


# instancia atletas
jorge = Atleta("Jorge")
jhon = Atleta("Jhon")

jorge.entrenar()
jorge.comer()
jorge.descansar()

jhon.entrenar()
jhon.comer()
jhon.descansar()

Atleta.incremento_fuerza_energia(10, 30)
jorge.entrenar()
jorge.descansar()

jhon.entrenar()
jhon.descansar()