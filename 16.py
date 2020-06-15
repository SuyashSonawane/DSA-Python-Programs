'''
Author: Tejas Morkar (https://github.com/tejasmorkar)
Question: Write a python program to store first year percentage of students in array. Write function
			for sorting array of floating point numbers in ascending order using quick sort and display
			top five scores
'''

def partition(arr,low,high): 
    i = ( low-1 )        
    pivot = arr[high]     
  
    for j in range(low , high): 
        if   arr[j] <= pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 

        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

def main():
	data = [float(i) for i in input("Enter the perecentage sperated by spaces: ").split() if i != ' ']
	quickSort(data, 0, len(data)-1)
	print("\nSorted Array: {}".format(data))
	top5 = data[-5:]
	top5.reverse()
	print("\nTop 5 Scores: {} {} {} {} {}".format(*top5))

if __name__ == "__main__":
	main()
