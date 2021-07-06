print('1.Create a lambda function that multiplies argument x with argument y')
a=lambda x,y: x*y
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
value=a(x,y)
print('value:',value)
print('\n2.Write a Python program to create Fibonacci series to n using Lambda')
def fibonacci(n):
    fib_list = [0,1]
    any(map(lambda _:fib_list.append(sum(fib_list[-2:])),range(2,n)))
    return fib_list[:n]
n=int(input('enter the size of n:')) 
print('****FIBONACCI SEQUENCE of',n,'****\n',fibonacci(n))
print('\n3.Write a Python program that multiply each number of given list with a given number')
lst=[2,18,12,5,9,0]
print('\n*******ORIGINAL LIST******\n',lst)
y=int(input('\n\nEnter no to multiply in list:'))
l=list(map(lambda x:x*y,lst))
print('\nlist after maping:',l)
print('\n4.Write a Python program to find numbers divisible by 9 from a list of numbers')
l1=list(filter(lambda x:(x%9==0),lst))
print('\nNumbers divisible by 9 from the list are:',l1)
print('\n5.Write a Python program to count the even numbers in a given list of integers')
l2=list(filter(lambda x:x%2==0,lst))
print('\nEven numbers in a given list is:',l2)
print('\nNo of even numbers in a list is:',len(l2))
print('\t\t*******END********')        
        
