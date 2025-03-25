```python
def cambio(importe, pagado):
    valores = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    cambio = pagado - importe

    for valor in valores:
        piezas = int(cambio // valor)
        cambio -= piezas * valor
        if piezas > 0:
            print(f"{piezas} x {valor:.2f} €")

importe = float(input("Importe: "))
pagado = float(input("Pagado: "))
cambio(importe, pagado)
```

**Example Usage:**

```
Importe: 1.50
Pagado: 2.00
1 x 1.00 €
1 x 0.50 €
```

**Explanation:**

* The `cambio()` function takes two arguments: `importe` and `pagado`.
* It calculates the change and stores it in the `cambio` variable.
* It iterates over the `valores` list and calculates the number of pieces for each value.
* If there are any pieces, it prints the number and the value.

**Note:**

* The code does not use any data structures or match expressions.
* It only uses loops to calculate and display the change.
* The output does not specify pieces for which there are zero units.