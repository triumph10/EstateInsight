from tkinter import *
from tkinter import messagebox
import ast
from maininterface import create_main_window


window=Tk()
window.title("SignUp")
window.geometry('900x700+350+150')
window.configure(bg='white')
window.resizable(False, False)
window_width = 1000
window_height = 660
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

#img PhotoImage(file='login.png')
img = PhotoImage(file='Images/estate.png')
Label(window,image=img,bg="white").place(x=170,y=200)

#image=img
frame=Frame(window,width=450,height=490,bg='white')
frame.place(x=480,y=50)

heading=Label(frame, text='Sign Up', fg="BLACK",bg="white", font=('Microsoft Yahei UI Light', 23,'bold'))
heading.place(x=100,y=2)


#create username
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

Frame(frame, width=295, height=2, bg="BLACK").place(x=25,y=177)

#Enter name
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

#create password
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

#confirm password
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

#signup button

def new_window():
    window.withdraw()  # Hide the main window
    main_window = create_main_window(window)
    main_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(window, main_window))


def close_windows(main_window, popup_window):
    popup_window.destroy()
    main_window.destroy()
Button(frame, width=39, pady=7,text='Sign Up', bg='#B31312',fg='white', border=0,command=new_window).place(x=35,y=390)

#I have an acc
label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light',9))
label.place(x=90,y=440)

#Login button
signin= Button(frame, width=6, text='Log in', border=0, bg='#B31312', cursor='hand2', fg='white')
signin.place(x=200,y=440)
window.mainloop()