from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *


root = Tk()
root.attributes('-fullscreen',True)

#***********************************
#Background image
bg = PhotoImage(file = "Background_1.png")
label = Label(root,image=bg)
label.place(x=0, y=0)

#**************************************

#Single correct multiple choice question
label1=Label(root,text= 'All questions are mandatory',background='light blue')
label1.pack(ipadx=10,ipady=10)
msg=Label(root,text="Who developed the Python language?")
msg.pack()

score = 0
def singlecrt():
    global score
    if v.get()=="3" :        
        score+=1
        print(score)
v = StringVar(root, "1")
values = {"Zim Den" : "1",
        "Niene Stom" : "2",
        "Guido van Rossum" : "3",
        "Wick van Rossum" : "4"}
for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5)
but=Button(root,text="save",command=singlecrt)
but.pack()

#*************************
#Multiple correct answer question
def mget():
    global score
    if var1.get()==1 and var2.get()==1 and var3.get()==0 and var4.get()==0 :
        score+=1
l = Label(root, text='Which of the following are mutable data types ')
l.pack()
var1=IntVar()
Checkbutton1=Checkbutton(root,text="List",variable=var1)
var2=IntVar()
Checkbutton2=Checkbutton(root,text="Dictionary",variable=var2)
var3=IntVar()
Checkbutton3=Checkbutton(root,text="Tuples",variable=var3)
var4=IntVar()
Checkbutton4=Checkbutton(root,text="Sets",variable=var4)
Checkbutton1.pack()
Checkbutton2.pack()
Checkbutton3.pack()
Checkbutton4.pack()

b=Button(root,text="save",command=mget)
b.pack()

#***********************
#Descriptive question
l = Label(root, text='Lists are Mutable/Immutabe : ')
l.pack()
data=StringVar()
textbox1=Entry(root,textvariable=data)
textbox1.pack()
def my_func():
    global score
    if data.get()=="Mutable":
       score+=1
b=Button(root,command=my_func,text="save")
b.pack()

#***************************
#True or False question
def func1():
    global score
    score+=1
def func2():
    pass

msg=Label(root,text="GUI is easy to learn.")
msg.pack()
bt = Button(root, text="True", command=lambda: func1())
bt.pack()
btn =Button(root, text="False", command=lambda: func2())
btn.pack()

#*******************
#Message box to display score
def func():
    global score
    showinfo("Your Score:",score)
word=Label(root,text="   " )
word.pack()
button1 =Button(root, text="Submit",command=lambda: func())
button1.pack(ipadx=20,ipady=30)
#**********************
#Menu bar
mailid='practicetest@gmail.com'

def functi():
    showinfo("Mail id",mailid)

menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Exit', command = root.destroy)


Contactus=Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Contact us', menu = Contactus)
Contactus.add_command(label ='Contact us', command = lambda: functi())
root.config(menu = menubar)


root.mainloop()