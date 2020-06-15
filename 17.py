'''
Author: Tejas Morkar (https://github.com/tejasmorkar)
Question: Write a python program to store 12th class percentage of students in array. Write
			function for sorting array of floating point numbers in ascending order using bucket sort
			and display top five scores.
'''

def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x): 
	arr = [] 
	slot_num = 10 # 10 means 10 slots, each 
	# slot's size is 0.1 
	for i in range(slot_num): 
		arr.append([]) 

	# Put array elements in different buckets  
	for j in x: 
		index_b = int(j / slot_num)
		arr[index_b].append(j)

	# Sort individual buckets  
	for i in range(slot_num): 
		arr[i] = insertionSort(arr[i]) 

	# concatenate the result 
	k = 0
	for i in range(slot_num): 
		for j in range(len(arr[i])): 
			x[k] = arr[i][j] 
			k += 1
	return x 

def main():
	data = [float(i) for i in input("Enter the perecentage sperated by spaces: ").split() if i != ' ']
	bucketSort(data)
	print("\nSorted Array: {}".format(data))
	top5 = data[-5:]
	top5.reverse()
	print("\nTop 5 Scores: {} {} {} {} {}".format(*top5))

if __name__ == "__main__":
	main()
