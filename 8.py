'''
Author: Tejas Morkar (https://github.com/tejasmorkar)
Question: Write a python program that determines the location of a saddle point of matrix if one
			exists. An m x n matrix is said to have a saddle point if some entry a[i][j] is the smallest
			value in row i and the largest value in j. 
'''

def inputMatrix(rows, cols):
	mat = []
	for i in range(rows):
		mat.append(list(map(int, input("Enter all the {0} elements with spaces of row {1}: ".format(cols, i)).split())))
	return mat

def main():
	rows = int(input("Enter the number of rows: "))
	cols = int(input("Enter the number of columns: "))

	mat = inputMatrix(rows, cols)

	flag = 0
	for i in range (rows):
		for j in range (cols):
			if mat[i][j] == min(mat[i]):
				if mat[i][j] == max([k[j] for k in mat]):
					flag = 1
					print("\nSaddle point found at {0}, {1}".format(i+1, j+1))
				break
	if flag == 0:
		print("No saddle point exists")


if __name__ == "__main__":
	main()
