#Write a Python program to store marks scored in subject “Fundamental of Data
#Structure” by N students in the class. Write functions to compute following:
#--a) The average score of class
#--b) Highest score and lowest score of class
#--c) Count of students who were absent for the test
#d) Display mark with highest frequency

sum = 0
abcnt = 0

dsa = list()
markslist = list()
counts = dict()

n = input('Enter the number of students:')
for i in range(int(n)):
    marks = input('Marks:')
    dsa.append(marks)
    try:
        m = int(marks)
        markslist.append(m)
        sum = sum + m
#        print(sum)
        counts[marks] = counts.get(marks,0) + 1
    except:
        if(marks == 'a') or (marks == 'A'):
            abcnt = abcnt + 1
avg = sum/int(n)
print('------------------------------------------------------------------------------------------------------')
print('All student markList     ',dsa)
print('Number Mark List         ',markslist) #Excluding students who were absent
print('average of ',n,'students is', avg)
print('Maximum Marks:           ',max(markslist))  # using the max(arg) function to calculate maximum in the list
print('Minimum Marks:           ',min(markslist)) # using the min(arg) function to calculate minimum in the list
print('Absent Count:            ', abcnt)
sortedict = sorted(counts.items())
print('Frequency list:          ',sortedict)
maxval = 0
for key,value in sortedict:
    if value > maxval:
        maxval = value
        maxkey = key
print('the Maximum marks are',maxkey,'with a frequency of',maxval)
print('------------------------------------------------------------------------------------------------------')