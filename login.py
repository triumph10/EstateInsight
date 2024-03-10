from tkinter import *
from tkinter import messagebox
from maininterface import create_main_window

window=Tk()
window.title('Login')
window.geometry('925x500+300+200')
window.configure(bg="white")
window.resizable(False, False)

img = PhotoImage(file='Images/estate.png')
Label(window,image=img,bg="white").place(x=150,y=150)

frame=Frame(window,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame, text='LOGIN', fg='BLACK', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100,y=5)

#Username column code
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
       user.insert(0,'Username')

user= Entry(frame, width=25,fg='black', border=0,bg="white", font=('Microsoft YaHei UI Light',11))
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

password=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
password.place(x=30,y=150)
password.insert(0,'Password')
password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#Button Code

def new_window():
    window.withdraw()  # Hide the main window
    main_window = create_main_window(window)
    main_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(window, main_window))

def close_windows(main_window, popup_window):
    popup_window.destroy()
    main_window.destroy()

    log_butt = Button(frame,width=39,pady=7,text='LOGIN',bg='#B31312',fg='white',border=0, command=new_window)
    log_butt.place(x=35,y=204)
    label2=Label(frame,text="Dont have an account?",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label2.place(x=75,y=270)

    signup=Button(frame,width=6,text="Sign in",border=0,bg='#B31312',cursor='hand2',fg='white')
    signup.place(x=215,y=270)

window.mainloop()