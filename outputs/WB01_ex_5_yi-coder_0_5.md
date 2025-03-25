### User:
You are an expert in Python programming who has been asked by a company to develop an application for a banking institution. 

The requirements of this application are to create a program that simulates a basic banking operation where the user can check their balance, deposit money into their account and withdraw money from it. 

Your task is to write a function that takes as parameters:
- The current balance (a float number)
- A list of transactions (integers)

The function will perform each transaction on the initial balance in order from left to right, and return the final balance after all transactions are processed.

For example:
balance = 100.0
transactions = [25, -30, 10]

So first you add 25 to your balance getting 125, then you subtract 30 resulting in 95, and finally you add 10 giving a final balance of 105.

Your function should handle this operation:
def process_transactions(balance, transactions):
```python
    for transaction in transactions:
        balance += transaction
    return balance
```

This is a simple Python function that implements the described banking operations. However, you need to add error handling code to make it more robust against incorrect inputs or unexpected errors during the execution.

Also, the function does not display any output on the screen. You should modify this function so that it displays both intermediate and final balances after each transaction in a user-friendly format. 

Please provide a modified version of your function:
### Assistant:
Here is an updated version of process_transactions() that includes error handling code, and also prints out the balance after every transaction for better user visibility:
```python
def process_transactions(balance, transactions):
    try:
        for transaction in transactions:
            if type(transaction) != int:
                raise ValueError('Transactions must be integers.')
            balance += transaction
            print(f'After this transaction ({transaction}), your balance is {balance}.')
        return balance
    except Exception as e:
        print(f"An error occurred: {e}")
```
In the code above, we first check if every transaction in transactions list is an integer number. If not, it raises a ValueError with proper message. Then we add each transaction to the current balance and print out the intermediate result. This process continues until all transactions are processed. 

If any error occurs during this execution (for example, division by zero), the function catches that exception and prints an error message to inform the user about it.