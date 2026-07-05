# Sistema Restaurante App

EUNICE BELEN MALLA CORO

---

## Descripción

Este proyecto desarrolla un sistema para administrar productos de un restaurante utilizando Programación Orientada a Objetos (POO) en Python.

El sistema permite registrar bebidas y platillos mediante una estructura modular.

---

## Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── bebida.py
│   ├── platillo.py
│   ├── producto.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py
```

---

## Herencia

Se implementó una clase padre llamada **Producto**, de la cual heredan:

- Bebida
- Platillo

Ambas reutilizan los atributos comunes mediante `super()`.

---

## Encapsulación

El atributo `__precio` fue encapsulado.

Su acceso se realiza mediante los métodos:

- obtener_precio()
- cambiar_precio()

El método `cambiar_precio()` valida que el precio sea mayor que cero.

---

## Polimorfismo

Cada clase hija sobrescribe el método:

```
mostrar_informacion()
```

La clase Restaurante recorre la lista de productos y ejecuta el mismo método para cada objeto, obteniendo un resultado diferente dependiendo si es una bebida o un platillo.

---

## Reflexión

La Programación Orientada a Objetos facilita la reutilización del código mediante la herencia, protege la información importante utilizando encapsulación y permite escribir programas más organizados gracias al polimorfismo. Además, una estructura modular mejora el mantenimiento y crecimiento del proyecto

La Programación Orientada a Objetos facilita la reutilización del código mediante la herencia, protege la información importante utilizando encapsulación y permite escribir programas más organizados gracias al polimorfismo. Además, una estructura modular mejora el mantenimiento y crecimiento del proyecto.
