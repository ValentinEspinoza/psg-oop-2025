class Celula:
    def __init__(self, adn, tipo_celula, energia_inicial=0.0):
        self.__adn = adn
        self.__tipo_celula = tipo_celula
        self.__energia = energia_inicial

    # propiedades
    @property
    def adn(self):
        return self.__adn  # solo lectura

    @property
    def tipo_celula(self):
        return self.__tipo_celula

    @tipo_celula.setter
    def tipo_celula(self, nuevo_tipo):
        self.__tipo_celula = nuevo_tipo

    @property
    def energia(self):
        return self.__energia  # solo lectura

    # metodos
    def comer(self, cantidad):
        if cantidad > 0:
            self.__energia += cantidad

    def dividirse(self):
        if self.__energia >= 10:
            nueva_energia = self.__energia / 2
            self.__energia = nueva_energia
            return Celula(self.__adn, self.__tipo_celula, nueva_energia)
        else:
            return None


# implementando la clase
celula1 = Celula("ABC-55", "Epitelial", 20)
print(f"ADN: {celula1.adn}")
print(f"Tipo: {celula1.tipo_celula}")
print(f"Energía: {celula1.energia}")

celula1.comer(5)
print(f"Energia despues de comer: {celula1.energia}")

celula2 = celula1.dividirse()
if celula2:
    print(f"Nueva celula con energia: {celula2.energia}")

celula1.tipo_celula = "Muscular"
print(f"Nuevo tipo de celula: {celula1.tipo_celula}")
