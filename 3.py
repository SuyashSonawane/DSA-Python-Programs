#Write a Python program for department library which has N books, write functions for following: 
#--a) Delete the duplicate entries 
#--b) Display books in ascending order based on cost of books 
#--c) Count number of books with cost more than 500.  
#d) Copy books in a new list which has cost less than 500. 
lib = dict()
lessCost = 0
moreCost = 0
lessCostList = list()
def duplicate():        #function to prevent duplication of books
    lib[bknm] = lib.get(bknm,cost)

n = input('Enter the number of books:')
for i in range(int(n)):
    bknm = input('Enter book name:')
    cst = input('Enter Book cost:')
    cost = int(cst)
    duplicate()     #calling duplicate function in runtime to check for duplication in runtime.
    if cost < 500:
        lessCost += 1
        lessCostList.append(bknm)
    else : moreCost += 1
sorted_lib = sorted((key,val) for (val,key) in lib.items())
print(type(sorted_lib))
print('Dictionary in sorted order is:',sorted_lib)
print('Number books with cost more than 500 is:',moreCost)
print('Number books with cost less than 500 is:',lessCost)
print('Names off books with cost less than 500 is:',lessCostList)
