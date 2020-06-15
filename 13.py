'''
Author: Tejas Morkar (https://github.com/tejasmorkar)
Question: Write a python program to maintain club members, sort on roll numbers in ascending
			order. Write function “Ternary_Search” to search whether particular student is member
			of club or not. Ternary search is modified binary search that divides array into 3 halves
			instead of two
'''

def ternary_search (L, key):
   left = 0
   right = len(L) - 1
   while left <= right:
      ind1 = left
      ind2 = left + (right - left) // 3
      ind3 = left + 2 * (right - left) // 3
      if key == L[left]:
         print("Roll number {} is in the club".format(key))
         return
      elif key == L[right]:
         print("Roll number {} is in the club".format(key))
         return
      elif key < L[left] or key > L[right]:
         print("Roll number {} is NOT in the club".format(key))
         return
      elif key <= L[ind2]:
         right = ind2
      elif key > L[ind2] and key <= L[ind3]:
         left = ind2 + 1
         right = ind3
      else:
         left = ind3 + 1
   return

def main():
	n = int(input("Enter the number of students in club: "))
	club = {"name": {}, "prn": {}, "roll": {}}

	for i in range(n):
		club["name"][i] = input("\nEnter the name of Student: ")
		club["prn"][i] = input("Enter the PRN of Student: ")
		club["roll"][i] = int(input("Enter the Roll Number of Student: "))

	while True:
		ar = [club["roll"][k] for k in club["roll"]]
		ar.sort()

		key = int(input("\nEnter the roll number of the student to be searched: "))

		ternary_search(ar, key)

		ch = input("Do you want to search another roll number? (y/n): ")

		if ch != 'y' and ch != 'Y':
			print("Program Terminated")
			break

if __name__ == "__main__":
	main()
