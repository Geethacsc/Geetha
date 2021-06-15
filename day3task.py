from tkinter import*
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('500x550')
#Declaring Window Color
window.configure(background = "purple");
#below four fields are declared
Name = Label(window ,text = "Employee Name").grid(row = 0,column = 0)
Id = Label(window ,text = "Employee id").grid(row = 1,column = 0)
Account_detail = Label(window ,text = "Account no").grid(row = 2,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 3,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 4,column = 0)
Birthdate = Label(window ,text = "D.O.B").grid(row =5 ,column = 0)
Income = Label(window ,text = "Annual income").grid(row = 6,column = 0)
PF = Label(window ,text = "Profident fund").grid(row = 7,column = 0)
PT = Label(window ,text = "Professional Tax").grid(row = 8,column = 0)
LFW = Label(window ,text = "Labour Welfare Fund").grid(row = 9,column = 0)
ESI = Label(window ,text = "Employee State Insurance").grid(row = 10,column = 0)

Name1 = Entry(window).grid(row = 0,column = 1)
ID1 = Entry(window).grid(row = 1,column = 1)
Account_detail1 = Entry(window).grid(row = 2,column = 1)
Email1 = Entry(window).grid(row = 3,column = 1)
Mobile1 = Entry(window).grid(row = 4,column = 1)
Birthdate1 = Entry(window).grid(row = 5,column = 1)
Income = Entry(window).grid(row = 6,column = 1)
PF = Entry(window).grid(row = 7,column = 1)
PT = Entry(window).grid(row = 8,column = 1)
LF1 = Entry(window).grid(row = 9,column = 1)
EST = Entry(window).grid(row = 10,column =1)
#fubction declaration
def clicked():
    print('Welcome!' 'The data is included successfully')
Button(window ,text="Submit", command=clicked, width=25,bg='brown',fg='navy blue').grid(row=11,column=0)
window.mainloop()
