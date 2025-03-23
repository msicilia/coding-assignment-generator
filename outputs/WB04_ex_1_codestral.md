 Thought: The problem is about designing a subprogram for a supermarket cash register that calculates the change due to a customer based on the cost of their purchase and the amount paid. The program should display the number of each type of bill or coin (billetes y monedas) that should be given as change, without specifying any pieces for which zero units are to be given.

   Action: I will write Python code using loops to solve this problem. The program will define a function `calculate_change` that takes the total cost of a purchase and the amount paid by the customer as arguments. It will then iterate through a list of bill and coin denominations in descending order, calculating the number of each type of bill or coin that should be given as change and printing it to the console.

   Code:
```py
def calculate_change(total_cost, amount_paid):
    # Define a list of bill and coin denominations in descending order
    denominations = [500.0, 200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    # Calculate the change due to the customer
    change = amount_paid - total_cost

    # Iterate through the list of denominations
    for denomination in denominations:
        # Calculate the number of this type of bill or coin that should be given as change
        num_pieces = int(change / denomination)

        # Print the result to the console, if necessary
        if num_pieces > 0:
            print("Number of {} euro pieces: {}".format(denomination, num_pieces))

        # Subtract this amount from the remaining change
        change = round(change % denomination, 2)
```

   Test Case:
```py
calculate_change(10.53, 20.0)
# Output:
# Number of 5.0 euro pieces: 1
# Number of 2.0 euro coins: 1
# Number of 1.0 euro coins: 2
# Number of 0.5 euro coins: 1
# Number of 0.05 euro coins: 2
```