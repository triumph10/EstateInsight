from tkinter import *
from tkinter import messagebox
import ast
import mysql.connector
from mysql.connector import Error



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
        self.img = PhotoImage(file='Images/estate_size.png')
        Label(root, image=self.img, bg="white").place(x=170, y=200)

        # image=img
        frame = Frame(root, width=450, height=490, bg='white')
        frame.place(x=480, y=50)

        heading = Label(frame, text='Sign Up', fg="BLACK", bg="white", font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=100, y=2)

        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='ARYA#305#varun',
                database='estateinsights'
            )
            print("Connected to MySQL")
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Database Error", "Failed to connect to database")
            return

        # create username
        def on_enter(e):
            self.username.delete(0, 'end')

        def on_leave(e):
            if self.username.get() == '':
                self.username.insert(0, 'Create a new Username')

        self.username = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahel UI Light', 11))
        self.username.place(x=30, y=150)
        self.username.insert(0, 'Create a new Username')
        self.username.bind("<FocusIn>", on_enter)
        self.username.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="BLACK").place(x=25, y=177)

        # Enter name
        def on_enter(e):
            self.name_field.delete(0, 'end')

        def on_leave(e):
            if self.name_field.get() == '':
                self.name_field.insert(0, 'Enter your Name')

        self.name_field = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahel UI Light', 11))
        self.name_field.place(x=30, y=80)
        self.name_field.insert(0, 'Enter your Name')
        self.name_field.bind("<FocusIn>", on_enter)
        self.name_field.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

        # create password
        def on_enter(e):
           self.confirm_pass.delete(0, 'end')

        def on_leave(e):
            if self.confirm_pass.get() == '':
                self.confirm_pass.insert(0, 'Create Password')

        self.confirm_pass = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahel UI Light', 11))
        self.confirm_pass.place(x=30, y=220)
        self.confirm_pass.insert(0, 'Create Password')
        self.confirm_pass.bind("<FocusIn>", on_enter)
        self.confirm_pass.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

        # confirm password
        # def on_enter(e):
        #     user.delete(0, 'end')
        #
        # def on_leave(e):
        #     if user.get() == '':
        #         user.insert(0, 'Confirm Password')
        #
        # user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahel UI Light', 11))
        # user.place(x=30, y=300)
        # user.insert(0, 'Confirm Password')
        # user.bind("<FocusIn>", on_enter)
        # user.bind("<FocusOut>", on_leave)
        #
        # Frame(frame, width=295, height=2, bg="black").place(x=25, y=327)

        # signup button
        Button(frame, width=39, pady=7, text='Sign Up', bg='#B31312', fg='white', border=0,command=self.register).place(x=35, y=390)

        # I have an acc
        label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=90, y=440)

        # Login button
        login = Button(frame, width=6, text='Log in', border=0, bg='#B31312', cursor='hand2', fg='white',command=self.login_page)
        login.place(x=200, y=440)

    def register(self):
        name = self.name_field.get()
        username = self.username.get()
        password = self.confirm_pass.get()

        try:
            if self.conn.is_connected():
                pst = self.conn.cursor()
                sql_query = 'INSERT INTO signin (name,username,password) VALUES (%s,%s,%s)'
                pst.execute(sql_query, (name, username, password))
                self.conn.commit()
                messagebox.showinfo("", "Successfully Registered")

                # After successful registration, go to the login page
                self.login_page()

        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("", "Failed to register")

    def login_page(self):
        self.root.destroy()
        import login

root=Tk()
obj = signup(root)
root.mainloop()