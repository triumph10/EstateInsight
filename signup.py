from tkinter import *
from tkinter import messagebox
import ast
import mysql.connector as mysql


class signup:
    def __init__(self, root):
        self.root = root

        self.root.title("SignUp")
        self.root.geometry('900x700+350+150')
        self.root.configure(bg='white')
        self.root.resizable(False, False)
        self.root_width = 1000
        self.root_height = 660
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = int((screen_width - self.root_width) / 2)
        y_position = int((screen_height - self.root_height) / 2)

        self.root.geometry(f"{self.root_width}x{self.root_height}+{x_position}+{y_position}")

        # img PhotoImage(file='login.png')
        self.img = PhotoImage(file='Images/estate.png')
        Label(root, image=self.img, bg="white").place(x=170, y=200)

        # image=img
        frame = Frame(root, width=450, height=490, bg='white')
        frame.place(x=480, y=50)

        heading = Label(frame, text='Sign Up', fg="BLACK", bg="white", font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=100, y=2)

        # create username
        def on_enter(e):
            code.delete(0, 'end')

        def on_leave(e):
            if code.get() == '':
                code.insert(0, 'Create a new Username')

        code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahel UI Light', 11))
        code.place(x=30, y=150)
        code.insert(0, 'Create a new Username')
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="BLACK").place(x=25, y=177)

        # Enter name
        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Enter your Name')

        user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahel UI Light', 11))
        user.place(x=30, y=80)
        user.insert(0, 'Enter your Name')
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

        # create password
        def on_enter(e):
            confirm_pass.delete(0, 'end')

        def on_leave(e):
            if confirm_pass.get() == '':
                confirm_pass.insert(0, 'Create Password')

        confirm_pass = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahel UI Light', 11))
        confirm_pass.place(x=30, y=220)
        confirm_pass.insert(0, 'Create Password')
        confirm_pass.bind("<FocusIn>", on_enter)
        confirm_pass.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

        # confirm password
        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            if user.get() == '':
                user.insert(0, 'Confirm Password')


        #Login button
        signin= Button(frame, width=6, text='Log in', border=0, bg='#B31312', cursor='hand2', fg='white',command = "login")
        signin.place(x=200,y=440)






    def login_page(self):
        self.root.destroy()
        import login

root=Tk()
obj = signup(root)
root.mainloop()

