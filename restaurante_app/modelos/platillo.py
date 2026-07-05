from modelos.producto import Producto


class Platillo(Producto):
    """Clase hija que representa un platillo."""

    def __init__(self, nombre, precio, disponible, calorias):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    # Polimorfismo
    def mostrar_informacion(self):
        return (
            "----- PLATILLO -----\n"
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.obtener_precio():.2f}\n"
            f"Disponible: {self.disponible}\n"
            f"Calorías: {self.calorias} kcal"
        )