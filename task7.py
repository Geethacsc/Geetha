#calculate using function
def task7(n1,n2):
    print('Addition of two numbers is:',n1+n2)
    print('Subtraction of two numbers is:',n1-n2)
    print('Multiplication of two numbers is:',n1*n2)
    print('Division of two numbers is:',n1/n2)
def covid(name,t=98):
    if t>98:
        print(name,'has a HIGH FEVER!Possibility of being a covid victim')
    elif t<98:
        print(name,'has a HIGH FEVER! Possibility of being a covid victim')
    else:
        print(name,'has a Normal body temperature! Covid Negative')
n1=int(input('enter number 1:'))
n2=int(input('enter number 2:'))
task7(n1,n2)
print('______COVID TEST______')
n=int(input('How many people for covid test:'))
for i in range(n):
      covid(name=input('Enter name:'),t=int(input('enter body temperature:')))
      covid(name=input('enter name:'))
