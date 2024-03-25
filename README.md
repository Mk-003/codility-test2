#Transactions Bank Account
This is a Python implementation for calculating the final balance of a bank account, given a list of transactions and their corresponding dates. The solution takes into account the monthly fee of 5 dollars for having a card, unless the monthly card payments cost at least 100 and there are at least three card payments within that month.

#Usage
To use the solution function, simply pass the list of transactions (amounts) and their corresponding dates (strings in YYYY-MM-DD format) as follows:

A = [100, 100, 100, -10]
D = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]

balance = solution(A, D)
print(balance)

This will output the final balance of the bank account.

#Implementation
The solution function calculates the balance by processing the transactions and deducting the monthly fees

#Dependencies
This implementation uses the datetime module to parse the transaction dates and check for the current month.