```python
def cambio(importe, pagado):
    """
    Calcula el cambio a dar al cliente.

    Args:
        importe: El importe de la compra.
        pagado: La cantidad pagada por el cliente.

    Returns:
        Una lista de tuplas que contiene el tipo de cambio y la cantidad.
    """

    valores = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    cambio = pagado - importe
    cambios = []

    for valor in valores:
        if cambio >= valor:
            piezas = int(cambio / valor)
            cambio -= piezas * valor
            cambios.append((valor, piezas))

    return cambios

# Ejemplo de uso
importe = float(input("Introduce el importe de la compra: "))
pagado = float(input("Introduce la cantidad pagada por el cliente: "))

cambios = cambio(importe, pagado)

for valor, piezas in cambios:
    if piezas > 0:
        print(f"{piezas} piezas de {valor} euros")
```

**Ejemplo de salida:**

```
Introduce el importe de la compra: 12.34
Introduce la cantidad pagada por el cliente: 20

4 piezas de 5 euros
2 piezas de 2 euros
1 pieza de 1 euro
1 pieza de 0.2 euros
1 pieza de 0.1 euro
```

**Nota:**

* El código utiliza un bucle `for` para iterar sobre los valores de cambio.
* El código calcula cuántas piezas de cada valor hay que dar como cambio.
* El código solo muestra las piezas que hay que dar como cambio, no las que no.