class Animal:
    origen = 'Feral'
    def __init__(self, especie, tipo, lugarEncontrado):
        self.especie = especie
        self.tipo = tipo
        self.lugarEncontrado = lugarEncontrado

animal1 = Animal("León", "Mamífero", "Sabana africana")
animal2 = Animal("Mono capuchino", "Mamífero", "Selva tropical")
animal3 = Animal("Serpiente pitón", "Reptil", "Bosque")
animal4 = Animal("Águila real", "Ave", "Montañas rocosas")

print("Mostrar zoologico...")
print("Animal 1: ",animal1.origen, animal1.especie, animal1.tipo, animal1.lugarEncontrado)
print("Animal 2: ",animal2.origen, animal2.especie, animal2.tipo, animal2.lugarEncontrado)
print("Animal 3: ",animal3.origen, animal3.especie, animal3.tipo, animal3.lugarEncontrado)
print("Animal 4: ",animal4.origen, animal4.especie, animal4.tipo, animal4.lugarEncontrado)

