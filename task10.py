print('\t\t_____________TASK 10_____________')
class Bank:
    def __init__(self,n,m,balance=0.0):
        self.acno=n
        self.name=m
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
        return self.balance
    def withdraw(self,amt):
        if amt>self.balance:
            print('\nSorry! Balance amt is less, so you cannot withdraw!')
        else:
            self.balance-=amt
            return self.balance
accno=input('Enter Account no: ')
name=input('Enter name: ')
b=Bank(accno,name)
flag='yes'
while flag=='yes':
    print('d-deposit,w-withdrawl')
    ch=input('Enter choice:')
    if ch=='d':
        amt=float(input('Enter amount to be deposited:'))
        print('Balance amount:',b.deposit(amt))
    else:
        amt=float(input('Enter amount to be withdrawn:'))
        print('Balance amount:',b.withdraw(amt))
    flag=input('Do you want to continue?yes/no:')
print('\t\t_______End______ ')  
