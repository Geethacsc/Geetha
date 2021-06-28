import re
choice='yes'
while choice=='yes':
    print('1.Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)')
    print("2.Write a Python program that matches a word containing 'ab'.")
    print('3.Write a Python program to check for a number at the end of a word/sentence.')
    print('4.Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.')
    print('5.Write a Python program to match a string that contains only uppercase letters.')
    ch=int(input('enter choice:'))
    if ch==1:
        print('1.match()\n2.search()\n3.findall()\n4.split()\n5.sub()')
        c=int(input('enter choice:'))
        if c==1:
            print("Match the alphanumerical word between 'j' and 'a' from the string.")
            str=input('enter string:')
            res=re.match(r'j\w*a',str)
            print(res)
            print(res.group())
        elif c==2:
            print("Search the first occurence of alphanumerical string between 'd' and 'l' from the str")
            str=input('enter string:')
            res=re.search(r'd\w*l',str)
            print(res.group())
        elif c==3:
            print("Findall the alpha numerical string between 'a' and 'e' from the string")
            str=input('enter string:')
            res=re.findall(r'a\w*e',str)
            print(res)
        elif c==4:
            print("Split the string into pieces when non alphanumeric characters are found")
            str=input('enter string:')
            res=re.split(r'\W+',str)
            print(res)
        elif c==5:
            print('Find the substring and replace it with new substring in the string')
            str=input('enter string:')
            s1=input('enter old string:')
            s2=input('enter string to replace:')
            res=re.sub(s1,s2,str)
            print(res)            
    elif ch==2:
        print('match the words that containing ab')
        str=input('enter string:')
        res=re.findall(r'\w*ab\w*',str)
        print(res)
    elif ch==3:
        print('Check whether the number is at the end of the word or string')
        str=input('enter string:')
        res=re.findall(r'([\w]*[0-9])',str)
        print(res)
    elif ch==4:
        str=input('enter string:')
        print('search the numbers within the length of 1 to 3 in the string')
        res=re.findall(r'\d\d\d',str)
        print(res)
    elif ch==5:
        print('match the uppercase words')
        str=input('enter string:')
        res=re.findall('([A-Z][A-Z]*)',str)
        print(res)
    else:
        print('WRONG CHOICE!')
    choice=input('Do you want to continue?yes\\no:')
print('end')
