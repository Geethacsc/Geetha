#How to print a value?
print('DAY 2 CHALLENGE')
print("30 days 30 hour challenge")
print('30 days 30 hour challenge')
#Assigning String to Variable:
Hours = "thirty"
print(Hours)
#Copy and paste above code , you will get error message as below.
#Try below:
Hours = "thirty"
print(Hours)
#Indexing using String:
Days = "Thirty days"
print(Days[0])
#Output will be T because Index value starts from 0. Try replacing some other number
#How to print the particular character from certain text?
Challenge = "I will win"
print(Challenge[7:10])
print(Challenge[3:9:2])
print(Challenge[3:])
print(Challenge[:6:])
print(Challenge[::8])
print(Challenge[::])
#Print the length of Character:
Challenge = "I will win"
print(len(Challenge))
#Convert String into lower character;
Challenge = "I will win"
print(Challenge.lower())
#String Concatenation – Joining two strings
a = "30 Days"
b = "30 hours"
c = a + b
print(c)
#Adding space during concatenation
a = "30 Days"
b = "30 hours"
c = a + " " + b
print(c)
#casefold() - Usage
text = "Thirty days and Thirty hours"
x = text.casefold()
print(x)
#Replace casefold with above values and execute it.
x= text.capitalize()
print(x)
y= text.find('ays')
print(y)
z= text.isalpha()
print(z)
a= text.isalnum()
print(a)

