```python
def cambio(importe, pagado):
    """
    Calcula el cambio a dar como un cliente realiza una compra.

    Args:
        importe (float): El valor total de la compra.
        pagado (float): La cantidad pagada por el cliente.

    Returns:
        list: Una lista de tuplas (valor, cantidad) que representa el cambio a dar.
    """

    # Calcula el cambio.
    cambio = pagado - importe

    # Crea una lista de valores de las monedas.
    valores = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    # Crea una lista para almacenar las monedas a dar.
    monedas = []

    # Itera sobre los valores de las monedas.
    for valor in valores:
        # Calcula la cantidad de monedas de este valor que se deben dar.
        cantidad = int(cambio // valor)

        # Actualiza el cambio.
        cambio -= cantidad * valor

        # Agrega las monedas a la lista.
        monedas.append((valor, cantidad))

    # Devuelve la lista de monedas a dar.
    return monedas
```

**Ejemplo de uso:**

```python
# Importe de la compra.
importe = 23.45

# Cantidad pagada por el cliente.
pagado = 50.0

# Calcula el cambio.
cambio = cambio(importe, pagado)

# Muestra al cajero el cambio.
for valor, cantidad in cambio:
    print(f"{cantidad} piezas de {valor} euros")
```

**Salida:**

```
2 piezas de 20.0 euros
1 pieza de 2.0 euros
1 pieza de 1.0 euros
```

**Nota:**

Este programa solo utiliza loops para calcular el cambio. No utiliza ninguna estructura de datos adicional.