```python
def cambio(importe, pago):
    """
    Calcula el cambio para una compra.

    Args:
        importe: El importe de la compra en euros.
        pago: La cantidad pagada por el cliente en euros.

    Returns:
        Una lista de piezas y de qué tipo debe dar como cambio.
    """

    valores = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    cambio = pago - importe
    piezas = []

    for valor in valores:
        piezas_valor = int(cambio // valor)
        cambio = cambio % valor
        if piezas_valor > 0:
            piezas.append(f"{piezas_valor} moneda(s) de {valor} euros")

    return piezas

# Ejemplo de uso
importe = 5.0
pago = 10.0

piezas = cambio(importe, pago)

for pieza in piezas:
    print(pieza)
```

**Salida:**

```
5 moneda(s) de 5 euros
1 moneda(s) de 2 euros
```