"""
@Author: Suyash Sonawane

Write a pythonprogram to store first year percentage of students in array. Write function
for sorting array of floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.
"""


def selectionSort(A):
    for i in range(len(A)):
        min_ = i
        for j in range(i + 1, len(A)):
            if A[min_] > A[j]:
                min_ = j
    A[i], A[min_] = A[min_], A[i]


def bubbleSort(A):
    for passnum in range(len(A) - 1, 0, -1):
        for i in range(passnum):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]


def main():
    percentages = []

    n = int(input("Enter number of students >>"))

    for _ in range(n):
        percentage = float(input(f"Enter percentage of {_}th student >>"))
        percentages.append(percentage)

    # selectionSort(percentages)
    bubbleSort(percentages)

    print(percentages)


if __name__ == "__main__":
    main()
