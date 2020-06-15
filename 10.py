"""
@Author: Suyash Sonawane
Write a python program for sparse matrix realization and operations on it- Transpose,
Fast Transpose and addition of two matrices 

"""


def displayMatrix(matrix):

    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()


def convertToSparseMatrix(matrix):

    sparseMatrix = []
    sparseMatrix.append([len(matrix), len(matrix[0]), 0])
    elements = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:

                temp = []

                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
                elements += 1
                sparseMatrix.append(temp)

    sparseMatrix[0][2] = elements
    return sparseMatrix


def simpleTranspose(matrix):
    transpose = []

    for row in matrix:
        row[0], row[1] = row[1], row[0]
        transpose.append(row)

    header = transpose.pop(0)
    transpose.sort()
    transpose.insert(0, header)

    return transpose


def fastTranspose(matrix):
    transpose = matrix
    index = [1]
    num_cols = matrix[0][1]
    num_terms = matrix[0][2]

    transpose[0], transpose[1] = transpose[1], transpose[0]

    row_terms = []

    for _ in range(num_cols):
        row_terms.append(0)
        index.append(0)

    for _ in range(1, num_terms):
        row_terms[matrix[_][1]] += 1

    for i in range(1, num_cols):
        index[i] = index[i - 1] + row_terms[i - 1]

    for i in range(1, num_terms):
        j = index[matrix[i][1]]
        index[matrix[i][1]] += 1

        transpose[j][0] = matrix[i][1]
        transpose[j][1] = matrix[i][0]
        transpose[j][2] = matrix[j][2]

    return transpose


def main():

    rows = int(input("Enter number of rows >>"))
    cols = int(input("Enter number of columns >>"))

    cols_array = []

    matrix = []

    for i in range(rows):
        for j in range(cols):
            val = int(input(f"Enter value for {i+1} , {j+1} >>"))
            cols_array.append(val)
        matrix.append(cols_array)
        cols_array = []

    print("Entered matrix\n")
    displayMatrix(matrix)

    print("\nSparse Matrix: ")
    sparseMatrix = convertToSparseMatrix(matrix)
    displayMatrix(sparseMatrix)

    print("\nTranspose Matrix: ")
    transposeMatix = simpleTranspose(sparseMatrix)
    displayMatrix(transposeMatix)


if __name__ == "__main__":
    main()
