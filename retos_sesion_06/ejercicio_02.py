class Departamento:
    def __init__(self, numero, inquilinos):
        self.numero = numero
        self.inquilinos = inquilinos  # lista de nombres

    def info(self):
        print(f"Departamento {self.numero}")
        print("Inquilinos:")
        for i in self.inquilinos:
            print(f" # {i}")
        print()


class Oficina:
    def __init__(self, numero, telefono):
        self.numero = numero
        self.telefono = telefono

    def info(self):
        print(f"Oficina {self.numero}")
        print(f"Teléfono: {self.telefono}\n")


class Piso:
    def __init__(self, numero):
        self.numero = numero
        self.departamentos = []  # lista de objetos departamento
        self.oficinas = []       # lista de objetos oficina

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def agregar_oficina(self, oficina):
        self.oficinas.append(oficina)

    def listar_unidades(self):
        print(f"Piso: {self.numero}")
        if self.departamentos:
            print("Departamentos:")
            for d in self.departamentos:
                d.info()
        else:
            print("No hay departamentos en este piso.\n")

        if self.oficinas:
            print("Oficinas:")
            for o in self.oficinas:
                o.info()
        else:
            print("No hay oficinas en este piso.\n")

    def info(self):
        self.listar_unidades()



class Edificio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.pisos = []  # lista de objetos Piso

    def agregar_piso(self, piso):
        self.pisos.append(piso)

    def listar_pisos(self):
        print(f"Edificio: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Cantidad de pisos: {len(self.pisos)}\n")
        for piso in self.pisos:
            piso.info()

    def info(self):
        self.listar_pisos()



# Uso

edificio = Edificio("Torre Illimani", "Av. Arce #1234, La Paz")
piso1 = Piso(1)
piso2 = Piso(2)
piso3 = Piso(3)

# departamentos y oficinas
dep101 = Departamento("101", ["Jhon Blanco", "Carlos Herrera"])
dep102 = Departamento("102", ["Juan Vargas"])
ofi1A = Oficina("1A", "72020202")

dep201 = Departamento("201", ["Juan Ramos"])
ofi2B = Oficina("2B", "75641123")
ofi2C = Oficina("2C", "72224334")

dep301 = Departamento("301", ["Maria Salazar", "Paola Espinoza"])
dep302 = Departamento("302", ["Fernando Blanco"])
ofi3A = Oficina("3A", "7253988")

# agrega unidades a los pisos
piso1.agregar_departamento(dep101)
piso1.agregar_departamento(dep102)
piso1.agregar_oficina(ofi1A)

piso2.agregar_departamento(dep201)
piso2.agregar_oficina(ofi2B)
piso2.agregar_oficina(ofi2C)

piso3.agregar_departamento(dep301)
piso3.agregar_departamento(dep302)
piso3.agregar_oficina(ofi3A)

# agrega pisos al edificio
edificio.agregar_piso(piso1)
edificio.agregar_piso(piso2)
edificio.agregar_piso(piso3)

# mostrar información del edificio
edificio.info()
