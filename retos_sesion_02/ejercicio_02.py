class Vino:
    def __init__(self, nombre, tipo, cepa, añoProduccion):
        self.nombre = nombre
        self.tipo = tipo
        self.cepa = cepa
        self.añoProduccion = añoProduccion

class Queso:
    def __init__(self, nombre, variedad, edad, contieneSal):
        self.nombre = nombre
        self.variedad = variedad
        self.edad = edad
        self.contieneSal = contieneSal


vino1 = Vino("Oporto", "Tinto", "Oporto", 2020)
vino2 = Vino("Chardonnay", "Blanco", "Chardonnay", 2021)
vino3 = Vino("Rosé del Valle", "Rosado", "Syrah", 2019)
vino4 = Vino("Cabernet selección", "Tinto", "Cabernet", 2018)

queso1 = Queso("Gouda", "Gouda", "6 meses", True)
queso2 = Queso("Roquefort azul", "Roquefort", "8 meses", True)
queso3 = Queso("Mozzarella", "Mozzarella", "2 semanas", False)

print("Mostrar Vinoteca...")
print("Vino 1: ",vino1.nombre, vino1.tipo, vino1.cepa, vino1.añoProduccion)
print("Vino 2: ",vino2.nombre, vino2.tipo, vino2.cepa, vino2.añoProduccion)
print("Vino 3: ",vino3.nombre, vino3.tipo, vino3.cepa, vino3.añoProduccion)
print("Vino 4: ",vino4.nombre, vino4.tipo, vino4.cepa, vino4.añoProduccion)

print("Queso 1", queso1.nombre, queso1.variedad, queso1.edad, queso1.contieneSal)
print("Queso 2", queso2.nombre, queso2.variedad, queso2.edad, queso2.contieneSal)
print("Queso 3", queso3.nombre, queso3.variedad, queso3.edad, queso3.contieneSal)