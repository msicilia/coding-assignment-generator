```
tc = 78
tf = int((9.0 * tc) / 5.0 + 32.0)
print(f"{tc} degrees Celsius is equivalent to {tf} degrees Fahrenheit.")

tc = tf
tf = int((tc * 5.0) / 9.0 + 32.0)
print(f"{tf} degrees Fahrenheit is equivalent to {tc} degrees Celsius.")
```
In this code, we define two variables `tc` and `tf` to represent the temperature in degrees Celsius and Fahrenheit, respectively. We then use the formula provided to convert between the two units. The output is displayed using formatted strings.

To test this code, you can try replacing the values of `tc` and `tf` with different numbers, such as 20 or 78, and see that the code correctly converts between the two units. You can also experiment with different values to see how the formula behaves.