'''
Author: Tejas Morkar (https://github.com/tejasmorkar)
Question: Write a Python program to compute following operations on String:
			a) To display word with the longest length
			b) To determines the frequency of occurrence of particular character in the string
			c) To check whether given string is palindrome or not
			d) To display index of first appearance of the substring
			e) To count the occurrences of each word in a given string
'''

import time

def showMenu():
	time.sleep(2) # to have a 1 second wait time before clearing screen
	print("\nMenu")
	print("----")
	print("1: Word with the longest length")
	print("2: Frequency of occurrence of a character in the given string")
	print("3: Check whether the string is Palindrome or not")
	print("4: Index of first appearance of the substring")
	print("5: Count of the occurences of each word in the string")
	print("6: Exit\n")

def wordWithLongestLen(data):
	wordsList = data.split()
	return max(wordsList, key=len)

def freqOfChar(data, character):
	freq = 0
	for ith_charachter in data:
		if ith_charachter == character:
			freq = freq + 1
	return freq

def is_palindrome(data):
	if data == data[::-1]:
		return True
	else:
		return False

def subStrAt(data, subStr):
	return data.find(subStr)

def freqOfWord(data, word):
	wordsList = data.split()
	return (wordsList.count(word))

def main():
	while True:
		showMenu()
		choice = input("Enter your choice from above (1-6): ")

		if choice == "1":
			# Word with the longest length
			data = input("Enter a sentence: ")
			print("The longest word is: '{}'".format(wordWithLongestLen(data)))
		elif choice == "2":
			# Frequency of a character in the given string
			data = input("Enter a string: ")
			character = input("Enter the character for which the frequency is to be found: ")
			print("Frequency of the character '{0}' is: '{1}'".format(character, freqOfChar(data, character)))
		elif choice == "3":
			# Check whether the string is Palindrome or not
			data = input("Enter a string: ")
			if is_palindrome(data):
				print("'{}' is a Palindrome string.".format(data))
			else:
				print("'{}' is NOT a Palindrome string.".format(data))
		elif choice == "4":
			# Index of first appearance of the substring
			data = input("Enter a string: ")
			subStr = input("Enter the substring for which the first index is to be found: ")
			print("First appearance of substring '{0}' is: '{1}'".format(subStr, subStrAt(data, subStr)))
		elif choice == "5":
			# Count of the occurences of each word in the string
			data = input("Enter a string: ")
			word = input("Enter the word for which the frequency is to be found: ")
			print("Frequency of the word '{0}' is: '{1}'".format(word, freqOfWord(data, word)))
		elif choice == "6":
			# Exit
			print("\nProgram Terminated Successfully")
			print("--------------------------------\n")
			break
		else:
			# Invalid Choice
			print("\nInvalid Choice, Please enter the choice between 1 to 6 only!\n")

if __name__ == "__main__":
	main()
