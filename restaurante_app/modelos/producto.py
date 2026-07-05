class Producto:
    """Clase padre que representa un producto."""

    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.__precio = precio
        self.disponible = disponible

    # Obtener el precio
    def obtener_precio(self):
        return self.__precio

    # Cambiar el precio validando que sea mayor que cero
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error: el precio debe ser mayor que cero.")

    # Método que será sobrescrito
    def mostrar_informacion(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Precio: ${self.__precio:.2f}\n"
            f"Disponible: {self.disponible}"
        )