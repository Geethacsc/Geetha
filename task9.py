import math
print('1.Write a program to loop through a list of numbers and add +2 to every value to elements in list')
l=[12,45,7,89,0,2]
l1=[]
print('list:',l)
for i in l:
    i=i+2
    l1.append(i)
print('new list:',l1)
print('\n2.Write a program to get the below pattern\n54321\n4321\n321\n21\n1')
print('***OUTPUT****')
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
print('3.Python Program to Print the Fibonacci sequence')
n=int(input('how many numbers:'))
n1,n2=0,1
c=0
if n<=0:
    print('please enter a positive integer')
elif n==1:
    print('Fibonacci sequence upto',n,':')
    print(n1)
#generate fibonacci sequence
else:
    print('FIBONACCI SEQUENCE:')
    while c<n:
        print(n1)
        nth=n1+n2
        #update values
        n1=n2
        n2=nth
        c+=1
print('\n4.Explain Armstrong number and write a code with a function')
print('\n*****DEFINITION*******')
print('\nA number is called ARMSTRONG NUMBER if it is equal to the sum of the cubes of its own digits')
num=int(input('\nenter a number:'))
sum=0
t=num
while t>0:
    digit=t%10
    sum+=digit**3
    t//=10
if num==sum:
    print(num,'is an Armstrong number')
else:
    print(num,'is not an Armstrong number')
#    ch=input('do you want to continue?yes/no:')
print('\n5.Write a program to print the multiplication table of 9')
t=int(input('enter size of the table:'))
for i in range(t):
    print('9*',i,'=',i*9)
print('\n6.Check if a program is negative or positive')
y=[]
for i in range(5):
    n=int(input('enter number:'))
    y.append(n)
    if n>0:
        print(n,'is POSITIVE NUMBER')
    elif n<0:
        print(n,'is NEGATIVE NUMBER')
    else:
        print('Number is ZERO')
print(y)
print('\n7.Write a program to convert the number of days to ages')
name=input('enter name:')
days=int(input('enter no of days:'))
age=days/365
print(name,'is',int(age),'years old')
print('\n8.Solve Trigonometry problem using math function write a program to solve using math function')
print('choose the above functions\n1.cos\n2.atan\n3.hypot\n4.sin\n5.degrees\n6.sec')
def tri(x,g):
    if x=='cos':
        print('math.cos(g):',math.cos(g))
    elif x=='atan':
        print('math.atan(g):',math.atan(g))
    elif x=='hypot':
        print('math.hypot(g):',math.hypot(g))
    elif x=='sin':
        print('math.sin(g):',math.sin(g))
    elif x=='degrees':
        print('math.degrees(g):',math.degrees(g))
    elif x=='ceil':
        print('math.ceil(g):',math.ceil(g))
    else:
        print('WRONG CHOICE!')
n=int(input('enter how many trignometric functions to find:'))
for i in range(n):
    x=input('enter the trignometric function:')
    g=int(input('enter the degree of function:'))
    tri(x,g)
print('9.Create a calculator only on a code level by using if condition (Basic arithmetic calculation')
choice='yes'
while choice=='yes':
    print('\n*******Choose the above choice*******')
    print('\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.EXPONENTIATION\n6.FLOOR DIVISION\n7.MODULUS DIVISION')
    ch=int(input('enter the choice:'))
    if ch in (1,2,3,4,5,6,7):
        N1=int(input('enter N1:'))
        N2=int(input('enter N2:'))
        if ch==1:
            print(N1,'+',N2,'=',N1+N2)
        elif ch==2:
            print(N1,'-',N2,'=',N1-N2)
        elif ch==3:
            print(N1,'*',N2,'=',N1*N2)
        elif ch==4:
            print(N1,'/',N2,'=',N1/N2)
        elif ch==5:
            print(N1,'**',N2,'=',N1**N2)
        elif ch==6:
            print(N1,'//',N2,'=',N1//N2)
        elif ch==7:
            print(N1,'%',N2,'=',N1%N2)
    else:
        print('WRONG CHOICE!')
    choice=input('Do you want to continue? yes/no:')
print('end')

