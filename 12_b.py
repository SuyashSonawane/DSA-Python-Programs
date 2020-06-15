"""
@Author :Suyash Sonawane

Write a python program to store names and mobile numbers of your friends in sorted
order on names. Search your friend from list using Fibonacci search. Insert friend if not
present in phonebook.
"""
phoneBook = [["Ramu", 123], ["Shamu", 456], ["Ramesh", 987], ["Shuresh", 11223344]]


def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)


def FibonacciSearch(arr, x):
    m = 0
    while FibonacciGenerator(m) < len(arr):  #
        m = m + 1
    offset = -1
    while FibonacciGenerator(m) > 1:
        i = min(offset + FibonacciGenerator(m - 2), len(arr) - 1)
        if x > arr[i][1]:
            m = m - 1
            offset = i
        elif x < arr[i][1]:
            m = m - 2
        else:
            return i
    if FibonacciGenerator(m - 1) and arr[offset + 1] == x:
        return offset + 1
    return -1


def main():

    query = int(input("Enter the number to be searched >> "))
    phoneBook.sort()

    index = FibonacciSearch(phoneBook, query)

    if index >= 0:
        print(f"{phoneBook[index]} is at index {index}")
    else:
        print("Contact not found")

        ui = input("Do you want to add this as new contact ? (y/n)>>")

        if ui == "y":
            name = input("Enter name for the contact >>")
            phoneBook.append([name, query])
            print("Contact added!")


if __name__ == "__main__":
    main()
