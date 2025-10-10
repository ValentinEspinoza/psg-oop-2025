class Cocinero:
    recetas = {
        "pan": {"harina", "agua"},
        "pizza": {"harina", "agua", "sal", "tomate", "queso"},
        "galleta": {"harina", "agua", "sal", "chocolate"}
    }

    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = set()
        self.productividad = 0

    def agregarIngredientes(self, lista):
        self.ingredientes.update(lista)

    def preparar(self, receta):
        if receta in Cocinero.recetas:
            requeridos = Cocinero.recetas[receta]
            if requeridos.issubset(self.ingredientes):
                self.productividad += 1
                print(f"{self.nombre} preparó {receta} ✅ | Productividad: {self.productividad}")
            else:
                print(f"{self.nombre} no tiene los ingredientes para {receta}. ❌")
        else:
            print(f"{receta} no es una receta válida.")

    
    @staticmethod
    def productividadTotal(listaCocineros):
        return sum(c.productividad for c in listaCocineros)


# instancia cocineros
jhon = Cocinero("Jhon")
jorge = Cocinero("jorge")
carla = Cocinero("Carla")

# se agregan los ingredientes
jhon.agregarIngredientes(["harina", "agua", "sal", "tomate", "queso"])
jorge.agregarIngredientes(["harina", "agua"])
carla.agregarIngredientes(["harina", "agua", "sal", "chocolate"])

# se preparan las recetas
jhon.preparar("pizza")
jorge.preparar("pan")
carla.preparar("galleta")


# metrica productividad
total = Cocinero.productividadTotal([jhon, jorge, carla])
print(f"📊 Productividad total: {total}")
