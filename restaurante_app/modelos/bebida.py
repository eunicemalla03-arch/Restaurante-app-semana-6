from modelos.producto import Producto


class Bebida(Producto):
    """Clase hija que representa una bebida."""

    def __init__(self, nombre, precio, disponible, volumen):
        super().__init__(nombre, precio, disponible)
        self.volumen = volumen

    # Polimorfismo
    def mostrar_informacion(self):
        return (
            "----- BEBIDA -----\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Disponible: {self.disponible}\n"
            f"Volumen: {self.volumen} ml"
        )