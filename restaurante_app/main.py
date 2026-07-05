from modelos.bebida import Bebida
from modelos.platillo import Platillo
from servicios.restaurante import Restaurante


# Crear el restaurante
restaurante = Restaurante()

# Crear bebidas
bebida1 = Bebida("Coca Cola", 2.50, "Sí", 500)
bebida2 = Bebida("Jugo Natural", 3.00, "Sí", 350)

# Crear platillos
platillo1 = Platillo("Hamburguesa", 8.50, "Sí", 750)
platillo2 = Platillo("Ensalada César", 6.75, "No", 420)

# Agregar productos al restaurante
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)
restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)

# Cambiar el precio utilizando encapsulación
bebida1.cambiar_precio(2.75)

# Mostrar todos los productos
restaurante.mostrar_productos()