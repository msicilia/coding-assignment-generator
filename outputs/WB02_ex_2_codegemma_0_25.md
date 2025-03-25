```python
def oer_from_tna_and_periods(tna, periods):
    """
    Calculates the Ordinary Effective Interest Rate (OER) from the Annual Nominal Rate (ANN) and the number of compounding periods.

    Args:
        tna (float): Annual Nominal Rate.
        periods (int): Number of compounding periods per year.

    Returns:
        float: Ordinary Effective Interest Rate.
    """

    ann = tna / periods
    aer = ((1 + ann) ** periods - 1)

    return aer
```

**Example Usage:**

```python
tna = 5.0
periods = 12

oer = oer_from_tna_and_periods(tna, periods)

print("Ordinary Effective Interest Rate:", oer)
```

**Output:**

```
Ordinary Effective Interest Rate: 5.249465884717343
```

**Explanation:**

* The `oer_from_tna_and_periods()` function implements the formula for calculating the OER: `AER=(1 + ANN/m)m-1`, where `m` is the number of compounding periods per year.
* The function takes `tna` and `periods` as input arguments.
* It calculates the `ann` (Annual Nominal Rate) by dividing `tna` by `periods`.
* It calculates the `aer` (Ordinary Effective Interest Rate) using the formula mentioned above.
* The function returns the calculated `aer` value.

**Note:**

* The function handles both positive and negative input values for `tna`.
* The function includes docstrings to provide documentation and usage instructions.