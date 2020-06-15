"""
@Author: Suyash Sonawane (https://github.com/SuyashSonawane)

Write a python program to compute following computation on matrix:
a) Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix
"""


def acceptMatrix():
    matrix = []
    rows = int(input("Enter number of rows >>"))
    cols = int(input("Enter number of cols >>"))

    for i in range(rows):
        temp = []
        for j in range(cols):
            temp.append(int(input(f"Enter the {i},{j} element >>")))
        matrix.append(temp)

    return matrix


def displayMatrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=" ")
        print("")


def add(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Shape Mismatch")
        return

    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] += m2[i][j]

    displayMatrix(m1)


def subtract(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Shape Mismatch")
        return

    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] -= m2[i][j]

    displayMatrix(m1)


def multiply(m1, m2):
    if len(m1[0]) != len(m2):
        print("Shape Mismatch")
        return

    matrix = []
    for i in range(len(m1)):
        temp = []
        for j in range(len(m2[0])):
            temp.append(0)
        matrix.append(temp)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum = 0
            for k in range(len(m1[0])):
                sum += m1[i][k] * m2[k][j]
            matrix[i][j] = sum

    displayMatrix(matrix)


def transpose(m):
    matrix = []
    for i in range(len(m)):
        temp = []
        for j in range(len(m[0])):
            temp.append(0)
        matrix.append(temp)

    for i in range(len(m)):
        for j in range(len(m[0])):
            matrix[j][i] = m[i][j]

    displayMatrix(matrix)


def main():
    # Accepting Matrix
    print("1st matrix")
    matrix1 = acceptMatrix()
    print("2nd matrix")
    matrix2 = acceptMatrix()

    print("Addition of matrix")
    add(matrix1, matrix2)

    print("Subtraction of matrix")
    subtract(matrix1, matrix2)

    print("Multiplication of matrix")
    multiply(matrix1, matrix2)

    print("Transpose of matrix")
    transpose(matrix1)


if __name__ == "__main__":
    main()
