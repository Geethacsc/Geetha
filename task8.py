from collections import Counter
import statistics
print('______1.Write a Python script to merge two Python dictionaries_______')
d1={'Korea':'Dream','India':'Gift','US':'Escape','Germany':'Other Choice'}
d2={'Pain':'V','Crush':'Kim bum','Love':'Imagination','Hate':'Myself','Dream':'Find WAY!','Forget':'Past','Heart':'World Wonder'}
print('\nd1:',d1)
print('\nd2:',d2)
print('\n*********DICTIONARY AFTER MERGING TWO DICTIONARIES**********\n')
d={**d1,**d2}
print('d:',d)
print('\n________Write a program to sort the value from descending to ascending in list and convert it in to a set_______')
L=['love','hate','143','pain','553','lone...ly','fun']
print('\nlist:',L)
L.sort()
print('\nlist after sorting in Ascending order:',L)
print('\nsort the value from descending to ascending in list')
L.sort(reverse=True)
print(L)
print('\nCONVERT LIST INTO SET')
print(set(L))
print('\nnumber of items in a dictionary key:')
v=d.values()
l=list(v)
#list number of items in a dictionary key
print(l)
print('\nlength of the list')
print(len(l))
print('\n________sort the list with the help of a function & without the function________')
l1=sorted(l)
print('\nsorting the list without using the function:')
print(l1)
def sort():
    l.sort()
    print(l)
print('\nsorting the list using function:')
sort()
print('\n_____Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input_____')
s=input('\nenter the main string:')
print('get a string from a given string')
x=input('enter the string to find:')
if len(x)==-1:
    print('string is not found')
else:
    print('string is found at position:',s.find(x))
s1=input('enter old string:')
s2=input('enter string to replace:')
print('new string:',s.replace(s1,s2))
print('\n \n_____Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter____')
print('\nstring after captilizing the first character:',s.title())
print('\n_______Write a Python program to find the repeated items of a list_____')
l1=[23,56,89,12,23,5,89,9]
print('\nnew list:',l1)
l2=[]
l3=[]
i=l1[0]
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        l3.append(i)
print('repeated items of a list is:')
print(l3)
print('\n______Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user____')
w=int(input('\nenter number 1:'))
p=int(input('enter number 2:'))
f=int(input('enter number 3:'))
print('sum of 3 numbers:',w+p
      +f)
v=int(input('enter number to divide the sum:'))
d=(w+p+f)/v
print('d=:',d)
print('\n_____find mean,median and of 3 elements_____')
num=[]
n=int(input('\n\nenter number of elements to calculate:'))
for i in range(n):
    num.append(int(input('enter no:')))   
sum=sum(num)
mean=sum/n
print('\nMEAN of given numbers is:',mean)
if n%2==0:
    m1=num[n//2]
    m2=num[n//2-1]
    median=(m1+m2)/2
else:
    median=num[n//2]
print('\nMEDIAN of given numbers is:',median)
c=Counter(num)
print(c)
m=statistics.mode(num)
print('MODE of given numbers:',m)
print('\n______Write a Python program to swap cases of a given string_______')
print('\nswap case of a string s is:',s.swapcase())
print('\n______Write a program to convert an integer to binary & octa decimal______')
c=int(input('\nenter the value of c:'))
print('\nBinary decimal of c is:',bin(c))
print('Octal decimal of c is:',oct(c))

