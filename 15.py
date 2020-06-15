#Write a python program to store second year percentage of students in array. 
#Write function for sorting array of floating point numbers in ascending order using  
# a) Insertion sort  
# b) Shell Sort and display top five score

import array
#----------------------------------------------------------------------
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

def insertionSortRecursive(arr,n):
    # base case
    if n<=1:
        return
     
    # Sort first n-1 elements
    insertionSortRecursive(arr,n-1)
    #Insert last element at its correct position in sorted array.
    last = arr[n-1]
    j = n-2
     
      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position 
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
 
    arr[j+1]=last
def printArray(arr,n):
    for i in range(n):
        print (arr[i], end = " ")

def shellSort(arr): 
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = int(n/2)
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j = j - gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap = int(gap/2)

marks = list()
n = int(input('Enter number of students:'))

for i in range(int(n)):
    mark = float(input('Enter marks of student: '))
    marks.append(mark)
arr = array.array('f',marks)

print('Original array:')
for i in range(int(n)):
    print(arr[i], end = " ")


insertionSort(arr) #calling insertion sort funtion
print ("\nNon Recursive insertion sorted array is:") 
for i in range(int(n)): 
    print (arr[i],end=" ") 


insertionSortRecursive(arr, n)
print("\nUsing recursive selection sort:")
printArray(arr, n)

shellSort(arr) 
print ("\nArray after Shell sorting:") 
for i in range(n): 
    print(arr[i], end = " ")