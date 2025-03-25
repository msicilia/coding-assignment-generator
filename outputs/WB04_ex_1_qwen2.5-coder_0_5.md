Entiendo su solicitud para diseñar un subprograma para una caja de supermercado que calcule el cambio basándose en los valores de monedas y billetes comunes en la Unión Europea. Voy a proporcionarle el código Python correspondiente, siguiendo las restricciones especificadas.

```python
def calculate_change(amount_due, amount_paid):
    # Lista de valores de monedas y billetes disponibles
    denominations = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    # Calcular el cambio
    change = amount_paid - amount_due

    # Imprimir el cambio
    print("Cambio a dar:")
    for denomination in denominations:
        if change >= denomination:
            num_pieces = int(change // denomination)
            change -= num_pieces * denomination
            if num_pieces > 0:
                print(f"{num_pieces} piezas de {denomination:.2f} euros")

# Ejemplo de uso
amount_due = float(input("Ingrese el importe en euros: "))
amount_paid = float(input("Ingrese la cantidad pagada en euros: "))

calculate_change(amount_due, amount_paid)
```

### Explicación del Código:

1. **Definición de Denominaciones**:
   - La lista `denominations` contiene los valores de monedas y billetes disponibles, ordenados desde el mayor al menor.

2. **Cálculo del Cambio**:
   - El cambio se calcula restando el importe debido (`amount_due`) de la cantidad pagada (`amount_paid`).

3. **Impresión del Cambio**:
   - Se itera a través de cada denominación en orden descendente.
   - Para cada denominación, se calcula cuántas unidades (piezas) son necesarias para dar el cambio restante.
   - Si la cantidad de piezas es mayor que cero, se imprime la información correspondiente.

4. **Ejemplo de Uso**:
   - El código solicita al usuario ingresar el importe en euros y la cantidad pagada.
   - Luego, llama a la función `calculate_change` para mostrar el cambio a dar.

Este código cumple con las restricciones especificadas (no se utilizan estructuras de datos complejas excepto iteraciones básicas) y muestra el cambio adecuado siguiendo los valores comunes en la Unión Europea.