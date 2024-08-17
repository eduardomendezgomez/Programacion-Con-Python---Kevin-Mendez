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

    def Dtipo(self):
        if self.peso > 10:
            return "Perro Grande"
        else:
            return "Perro Pequeño"
        
    def RegistrarPerro(self):
        estado = "Atendido"
        return estado
    def imprmirDatos(self):
        print(f"Nombre del perro: {self.nombre}")
        print(f"Edad del perro: {self.edad}")
        print(f"Peso del perro: {self.peso}")
        print(f"Raza del perro: {self.raza}")
        print(f"Color del perro: {self.color}")
        print(f"Dueño del perro: {self.dueno}")
        print(f"Tipo de perro: {self.tipo}")
        print(f"Estado del perro: {self.estado}")
        print("****************************************************")



nombre = input("Nombre del perrito: ")
edad = int(input("Edad del perrito: "))
peso = float(input("peso del perrito: "))
raza = input("Raza del perrito: ")
color = input("Color del perrito: ")
dueno = ("Nombre del dueño: ")
print("**************************************************")

nuevoPerro = Perro(nombre,edad,peso,raza,color,dueno)
nuevoPerro.imprmirDatos()