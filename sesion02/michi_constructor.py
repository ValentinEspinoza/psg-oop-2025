class Gato:
    especie = "felino"
    def __init__(self, color, genero, edad, castrado):
        self.color = color
        self.genero = genero
        self.edad = edad
        self.castrado = castrado

# Instanciar
michi = Gato("Negro", "hembra", 2, False)
miauricio = Gato("Naranja", "macho", 1, True)

# Mostrar atributos
print("Michi: ", michi.especie)
print(michi.color)
print(michi.genero)
print(michi.edad)
print(michi.castrado)

print("Miauricio: ", miauricio.especie)
print(miauricio.color)
print(miauricio.genero)
print(miauricio.edad)
print(miauricio.castrado)
print("Gato es: ", Gato.especie)