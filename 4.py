"""
@Author: Suyash Sonawane (https://github.com/SuyashSonawane)

Write a Python program that computes the net amount of a bank account based a
transaction log from console input. The transaction log format is shown as following: D
100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for
withdraw and deposit) D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be: 500

"""


def main():
    balance = 0  # Variable for holding balance
    transactions = int(input("Enter the number of transactions >> "))

    for _ in range(transactions):
        category, amount = input("Enter statements seperated by space >>").split(
            " "
        )  # accepting inputs from user
        amount = int(amount)

        if category == "D":
            balance += amount

        if category == "W":
            if balance - amount < 0:
                print("Withdrawal is not allowed if balance is going negative")
                continue
            else:
                balance -= amount

    print("Final Balance ", balance)


if __name__ == "__main__":
    main()
