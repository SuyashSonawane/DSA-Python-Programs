'''
Author: Tejas Morkar (https://github.com/tejasmorkar)
Question: It is decided that weekly greetings are to be furnished to wish the students having their
			birthdays in that week. The consolidated sorted list with desired categorical information
			is to be provided to the authority. Write a python program to store students PRNs with
			date and month of birth. Let List_A and List_B be the two list for two SE Computer
			divisions. Lists are sorted on date and month. Merge these two lists into third list
			“List_SE_Comp_DOB” resulting in sorted information about Date of Birth of SE Computer
			students
'''

import time

def showMenu():
	time.sleep(2) # to have a 1 second wait time before clearing screen
	print("\nMenu")
	print("----")
	print("1: Add data to SE A List")
	print("2: Add data to SE B List")
	print("3: Merge Lists")
	print("4: Display Final List")
	print("5: Exit\n")

def main():
	while True:
		showMenu()
		choice = input("Enter your choice from above (1-5): ")

		if choice == "1":
			# Add data to SE A List
			a = int(input("Enter number of students: "))

			List_A = []
			for i in range(a):
				prn = int(input("Enter the PRN: "))
				date = int(input("Enter the Date: "))
				month = int(input("Enter the Month in number format: "))
				List_A.append([prn, date, month])

			List_A = sorted(List_A, key = lambda x: (x[2],x[1]))

		elif choice == "2":
			# Add data to SE B List
			b = int(input("Enter number of students: "))

			List_B = []
			for i in range(b):
				prn = int(input("Enter the PRN: "))
				date = int(input("Enter the Date: "))
				month = int(input("Enter the Month in number format: "))
				List_B.append([prn, date, month])

			List_B = sorted(List_B, key = lambda x: (x[2],x[1]))

		elif choice == "3":
			# Merge Lists
			List_SE_Comp_DOB = List_A + List_B
			List_SE_Comp_DOB = sorted(List_SE_Comp_DOB, key = lambda x: (x[2],x[1]))
		elif choice == "4":
			# Display Final List
			for i in range(len(List_SE_Comp_DOB)):
				print("\n{}th Entry: ".format(i+1))
				print("PRN: ", List_SE_Comp_DOB[i][0])
				print("Date: ", List_SE_Comp_DOB[i][1])
				print("Month: ", List_SE_Comp_DOB[i][2])
		elif choice == "5":
			# Exit
			print("\nProgram Terminated Successfully")
			print("--------------------------------\n")
			break
		else:
			# Invalid Choice
			print("\nInvalid Choice, Please enter the choice between 1 to 5 only!\n")

if __name__ == "__main__":
	main()
