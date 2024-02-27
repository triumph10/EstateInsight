from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title("SignUp")
window.geometry('900x700+350+150')
window.configure(bg='#fff')
window.resizable(False, False)

#img PhotoImage(file='login.png')
Label(window,  border=0,bg='white').place(x=50,y=90)
#image=img
frame=Frame(window,width=450,height=490,bg='#fff')
frame.place(x=480,y=50)

heading=Label(frame, text='Sign up', fg="#57a1f8",bg="white", font=('Microsoft Yahei UI Light', 23,'bold'))
heading.place(x=100,y=2)
####--------------------------------------------
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    if code.get()=='':
        code.insert(0,'Create a new Username')

code = Entry(frame, width=25, fg='black', border=0, bg= 'white', font=('Microsoft Yahel UI Light',11))
code.place(x=30,y=150)
code.insert(0, 'Create a new Username')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=177)

####----------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Enter your Name')

user = Entry(frame, width=25, fg='black', border=0, bg= 'white', font=('Microsoft Yahel UI Light',11))
user.place(x=30,y=80)
user.insert(0, 'Enter your Name')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=107)
#--------------------------------------------------
def on_enter(e):
    confirm_pass.delete(0,'end')
def on_leave(e):
    if confirm_pass.get()=='':
        confirm_pass.insert(0,'Create Password')

confirm_pass = Entry(frame, width=25, fg='black', border=0, bg= 'white', font=('Microsoft Yahel UI Light',11))
confirm_pass.place(x=30,y=220)
confirm_pass.insert(0, 'Create Password')
confirm_pass.bind("<FocusIn>",on_enter)
confirm_pass.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=247)

####----------------------------------------
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0,'Confirm Password')

user = Entry(frame, width=25, fg='black', border=0, bg= 'white', font=('Microsoft Yahel UI Light',11))
user.place(x=30,y=300)
user.insert(0, 'Confirm Password')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25,y=327)


Button(frame, width=39, pady=7,text='Sign up', bg='#57a1f8',fg='white', border=0).place(x=35,y=390)

label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=440)

signin= Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8')
signin.place(x=200,y=440)
window.mainloop()