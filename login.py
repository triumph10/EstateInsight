from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#DFA878")
root.resizable(False, False)

img = PhotoImage(file='estate.png')
Label(root,image=img,bg="#DFA878").place(x=150,y=150)

frame=Frame(root,width=350,height=350,bg="#DFA878")
frame.place(x=480,y=70)

heading=Label(frame, text='LOGIN', fg='BLACK', bg='#DFA878', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)

#Username column code
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
       user.insert(0,'Username')

user= Entry(frame, width=25,fg='black', border=0,bg="#DFA878", font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#Password column code
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    name=password.get()
    if name=='':
       password.insert(0,'Password')

password=Entry(frame,width=25,fg='black',border=0,bg='#DFA878',font=('Microsoft Yahei UI Light',11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#Button Code
Button(frame,width=39,pady=7,text='LOGIN',bg='#B67352',fg='BLACK',border=0).place(x=35,y=204)
label2=Label(frame,text="Dont have an account?",fg='black',bg='#DFA878',font=('Microsoft Yahei UI Light',9))
label2.place(x=75,y=270)

signup=Button(frame,width=6,text="Sign in",border=0,bg='#B67352',cursor='hand2',fg='BLACK')
signup.place(x=215,y=270)


root.mainloop()