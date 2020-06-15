'''
Author: Tejas Morkar (https://github.com/tejasmorkar)
Question: a) Write a pythonprogram to store roll numbers of student in array who attended
			training program in random order. Write function for searching whether particular
			student attended training program or not, using Linear search and Sentinel search.
			b) Write a python program to store roll numbers of student array who attended training
			program in sorted order. Write function for searching whether particular student
			attended training program or not, using Binary search and Fibonacci search
'''

import time

def showMenu():
	time.sleep(2) # to have a 1 second wait time before clearing screen
	print("\nMenu")
	print("----")
	print("- A")
	print("1: Linear search")
	print("2: Sentinel search")
	print("- B")
	print("3: Binary search")
	print("4: Fibonacci search")
	print("5: Exit\n")

def main():
	while True:
		showMenu()
		choice = input("Enter your choice from above (1-5): ")

		if choice == "1":
			# Linear search
			data = list(map(int, input("Enter the roll numbers of students present sperated by spaces: ").split()))
			print("\nPresent Students : {}".format(data))

			roll = int(input("Enter the roll number of the student to be searched: "))

			flag = 0
			for i in range (len(data)):
				if data[i] == roll:
					flag = 1
					print("\nFound student at index: {}".format(i+1))
					break
			if flag == 0:
				print("\nNo match found")
		elif choice == "2":
			# Sentinel search
			data = list(map(int, input("Enter the roll numbers of students present sperated by spaces: ").split()))
			print("Present Students : {}".format(data))

			roll = int(input("Enter the roll number of the student to be searched: "))

			print(data[-1])
			last = data[-1]
			data[-1] = roll
			i = 0
		  
			while (data[i] != roll):
				i = i+1
		   
			data[-1] = last
		  
			if ((i < len(data)-1) or (roll == data[-1])) :
				print("\nFound student at index: {}".format(i+1))
			else:
				print("\nNo match found")
		elif choice == "3":
			# Binary search
			data = list(map(int, input("Enter the roll numbers of students present sperated by spaces: ").split()))
			data.sort()
			print("Present Students : {}".format(data))

			roll = int(input("Enter the roll number of the student to be searched: "))

			flag = 0
			low = 0
			high = len(data) - 1
			mid = 0

			while low <= high: 
				mid = (high + low) // 2

				if data[mid] < roll: 
					low = mid + 1

				elif data[mid] > roll: 
					high = mid - 1

				else: 
					flag = 1
					print("\nFound student at index: {}".format(mid+1)) 
					break

			if flag == 0:
				print("\nNo match found")
		elif choice == "4":
			# Fibonacci search
			data = list(map(int, input("Enter the roll numbers of students present sperated by spaces: ").split()))
			data.sort()
			print("Present Students : {}".format(data))

			roll = int(input("Enter the roll number of the student to be searched: "))

			index = fibMonaccianSearch(data, roll, len(data))

			if index == -1:
				print("\nNo match found")
			else:
				print("\nFound student at index: {}".format(index+1)) 
		elif choice == "5":
			# Exit
			print("\nProgram Terminated Successfully")
			print("--------------------------------\n")
			break
		else:
			# Invalid Choice
			print("\nInvalid Choice, Please enter the choice between 1 to 5 only!\n")

def fibMonaccianSearch(arr, x, n):  
    fibMMm2 = 0 # (m-2)'th Fibonacci No. 
    fibMMm1 = 1 # (m-1)'th Fibonacci No. 
    fibM = fibMMm2 + fibMMm1 # m'th Fibonacci 
   
    while (fibM < n): 
        fibMMm2 = fibMMm1 
        fibMMm1 = fibM 
        fibM = fibMMm2 + fibMMm1 
  
    offset = -1; 
  
    while (fibM > 1): 
          
        i = min(offset+fibMMm2, n-1) 
  
        if (arr[i] < x): 
            fibM = fibMMm1 
            fibMMm1 = fibMMm2 
            fibMMm2 = fibM - fibMMm1 
            offset = i 
  
        elif (arr[i] > x): 
            fibM = fibMMm2 
            fibMMm1 = fibMMm1 - fibMMm2 
            fibMMm2 = fibM - fibMMm1 
  
        else : 
            return i 
  
    if(fibMMm1 and arr[offset+1] == x): 
        return offset+1; 
  
    return -1

if __name__ == "__main__":
	main()
