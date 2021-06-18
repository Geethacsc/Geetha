l1=['2','lord','45','jg143','45']
for i in range(3):
    l1.append(input("enter the number to insert:"))
    print('new list:',l1)
choice='yes'
while choice=='yes':
    ch=(input('enter the choice:'))
    if ch in('1','2','3','4','5'):
        if ch=='1':
            l1.insert(3,'jissajesus')
            print('list after insertion:',l1)
        elif ch=='2':
            del l1[1:3]
            print('list after deletion:',l1)
        elif ch=='3':
            l2=['ahteeg','susej','alijiv',341]
            l1.extend(l2)
            print('list after extention:',l1)
        elif ch=='4':
            l1.pop()
            print('list after using pop function:',l1)
        elif ch=='5':
            y=input('enter the number to remove:')
            if y in l1:
                l1.remove(y)
                print('new list:',l1)
            else:
                print('given value is not in the list')
    else:
        print('WRONG CHOICE!')
    choice= input('do u want to continue:yes\no?')
print('____end of the loop____')
m1=max(l1)
m2=min(l1)
print('maximum variable in the list:',m1)
print('minimum variable in the list:',m2)
#tuple creation
x=('vg','674','45','@yh', 'ahteeg')
print('tuple:',x)
#reverse the tuple elements
a=reversed(x)
print('Reverse of tuple :',tuple(a))
# convertion of tuple into list
z=('456','tihr','tiger','#@bh')
print(list(z))
