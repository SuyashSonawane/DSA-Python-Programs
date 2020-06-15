"""
@Author: Suyash Sonawane
Write a python program to store names and mobile numbers of your friends in sorted
order on names. Search your friend from list using binary search (recursive and nonrecursive). Insert friend if not present in phonebook
"""
from math import floor


phoneBook = [["Ramu", 123], ["Shamu", 456], ["Ramesh", 987], ["Shuresh", 11223344]]


def recursiveBinarySearch(Array, L, R, x):
    if R >= L:
        mid = (L + (R - L)) // 2
        if Array[mid][1] == x:
            return mid
        elif Array[mid][1] > x:
            return recursiveBinarySearch(Array, L, mid - 1, x)
        else:
            return recursiveBinarySearch(Array, mid + 1, R, x)
    else:
        return -1


def binary_search(Array, x):
    n = len(Array)
    L = 0
    R = n - 1

    while L <= R:
        mid = floor((L + R) / 2)
        if Array[mid][1] < x:
            L = mid + 1
        elif Array[mid][1] > x:
            R = mid - 1
        else:
            return mid
    return -1


def main():

    query = int(input("Enter the number to be searched >> "))
    phoneBook.sort()

    # index = binary_search(phoneBook, query)
    index = recursiveBinarySearch(phoneBook, 0, len(phoneBook), query)

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
