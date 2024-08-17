class Perro: 
    def __init__(self,nombre,edad,peso,raza,color,dueno):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.raza = raza
        self.color = color
        self.dueno = dueno 
        self.estado = "No atendido"
        self.tipo = self.Dtipo()
#creando una funcion que defina conforme al peso si es mayor que 10 es  perro grande, sino, es perro pequeño
    def Dtipo(self):
        if self.peso > 10:
            return "Perro Grande"
        else:
            return "Perro Pequeño"
        
    def RegistrarPerro(self):
        estado = "Atendido"
        return estado


def IngresarPerro():
    nombre = input("Nombre del perrito: ")
    edad = int(input("Edad del perrito: "))
    peso = float(input("peso del perrito en kg: "))
    raza = input("Raza del perrito: ")
    color = input("Color del perrito: ")
    dueno = input("Nombre del dueño: ")
    print("**************************************************")
    nuevoPerro = Perro(nombre,edad,peso,raza,color,dueno)
    return nuevoPerro
def imprmirDatos(perro):
        print(f"Nombre del perro: {perro.nombre}")
        print(f"Edad del perro: {perro.edad}")
        print(f"Peso del perro: {perro.peso} kg")
        print(f"Raza del perro: {perro.raza}")
        print(f"Color del perro: {perro.color}")
        print(f"Dueño del perro: {perro.dueno}")
        print(f"Tipo de perro: {perro.tipo}")
        print(f"Estado del perro: {perro.estado}")
        print("****************************************************")

perro = IngresarPerro()
imprmirDatos(perro)