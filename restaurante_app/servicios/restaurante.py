class Restaurante:
    """Clase que administra los productos."""

    def __init__(self):
        self.productos = []

    # Agregar productos
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Mostrar todos los productos
    def mostrar_productos(self):
        print("\n========== MENÚ DEL RESTAURANTE ==========\n")

        for producto in self.productos:
            print(producto.mostrar_informacion())
            print("--------------------------------------")