  You are given a list of euro denominations in euros, and you must design a program that calculates the change for a customer who has paid a certain amount and returns the number of pieces (bills and coins) and their types that the cashier must give as change. The output should not include any units for which there is no change.

Here are some test cases:

Test case 1:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 10
Output: [('1', '1')]

Test case 2:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 60
Output: [('1', '1'), ('1', '2')]

Test case 3:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 90
Output: [('2', '1'), ('1', '2')]

Test case 4:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 70
Output: [('1', '2')]

Test case 5:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 80
Output: [('1', '3')]

Test case 6:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 95
Output: [('2', '3'), ('1', '3')]

Test case 7:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 100
Output: [('2', '3')]

Test case 8:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 130
Output: [('2', '3'), ('2', '4')]

Test case 9:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 160
Output: [('3', '4')]

Test case 10:
Input: 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01
Amount paid: 190
Output: [('4', '4')]

In the above test cases, you can see that the program must calculate the change for a customer who has paid a certain amount and return the number of pieces (bills and coins) and their types that the cashier must give as change. The output should not include any units for which there is no change.

You are given a list of euro denominations in euros, and you must design a program that calculates the change for a customer who has paid a certain amount and returns the number of pieces (bills and coins) and their types that the cashier must give as change. The output should not include any units for which there is no change.

You can assume that the input list will always be sorted in descending order, and that the amount paid by the customer will always be a valid denomination from the list of euro denominations.