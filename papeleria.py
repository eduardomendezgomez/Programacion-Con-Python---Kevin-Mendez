class Articulo:
    def __init__(self, nombre, marca, precio_compra):
        self.nombre = nombre
        self.marca = marca
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.30

    def __str__(self):
        return f"Nombre: {self.nombre}, Marca: {self.marca}, Precio de venta: {self.precio_venta}"

class Papeleria:
    def __init__(self):
        self.articulos = []

    def agregar_cuaderno(self, hojas):
        if hojas == 50:
            precio_compra = 5
        elif hojas == 100:
            precio_compra = 10
        cuaderno = Articulo("Cuaderno", "HOJITAS", precio_compra)
        self.articulos.append(cuaderno)

    def agregar_lapiz(self, tipo):
        if tipo == "grafito":
            precio_compra = 2
        elif tipo == "colores":
            precio_compra = 5
        lapiz = Articulo("Lapiz", "RAYAS", precio_compra)
        self.articulos.append(lapiz)

    def visualizar_articulos(self):
        for articulo in self.articulos:
            print(articulo)

papeleria = Papeleria()

while True:
    print("1. Agregar cuaderno")
    print("2. Agregar lapiz")
    print("3. Visualizar articulos")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        hojas = int(input("Ingrese el número de hojas del cuaderno (50 o 100): "))
        papeleria.agregar_cuaderno(hojas)
    elif opcion == "2":
        tipo = input("Ingrese el tipo de lapiz (grafito o colores): ")
        papeleria.agregar_lapiz(tipo)
    elif opcion == "3":
        papeleria.visualizar_articulos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")