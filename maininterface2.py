from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class maininterface2:
    def __init__(self, root):
        self.root = root
        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 15, "bold")

        one = Label(root,
                    text="EstateInsight",
                    bg="#B31312",
                    fg="white",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=1,
                    height=5)
        one.pack(fill=X, side=TOP)
        insertButt = Button(one,
                            text="Login",
                            bg="#B31312",
                            fg="white",
                            border=0,
                            activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=3, pady=2)
        insertButt = Button(one,
                            text="Sign Up",
                            bg="#B31312",
                            fg="white",
                            border=0,
                            activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=3, pady=2)

        # app color
        self.root.configure(bg='white')

        # setting up geometry for app
        window_width = 1000
        window_height = 660

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # setting up icon for window title
        icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, icon)

        # setting up the toolbar for the app
        toolbar = Frame(root, bg="white", relief=GROOVE, bd=2, pady=2)

        printButt = Button(toolbar,
                           text="Home",
                           bg="white",
                           border=0,
                           activebackground='#B67352', command=self.home)
        printButt.pack(side=LEFT, padx=20, pady=2)
        insertButt = Button(toolbar,
                            text="Buy",
                            bg="white",
                            border=0,
                            activebackground='#B67352',command = self.buy)
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Sell",
                           bg="white",
                           border=0,
                           activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Rent",
                           bg="white",
                           border=0,
                           activebackground='#B67352',command = self.rent)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Wishlist",
                           bg="white",
                           border=0,
                           activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Help",
                           bg="white",
                           border=0,
                           activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Search')

        user = Entry(self.root,
                     width=25,
                     fg='black',
                     bg="white",
                     relief=GROOVE,
                     font=('Microsoft YaHei UI Light', 11))
        user.place(x=400, y=100)
        user.insert(0, "Search")
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(root, width=203, height=2, bg='black').place(x=400, y=125)

        # setting up view points of app
        frame1 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       relief=GROOVE,
                       bd=1
                       )
        frame1.place(relx=0.1, rely=0.25)

        self.left_image = PhotoImage(file='Images/estate.png')
        self.left_image_label = Label(frame1,
                                 image=self.left_image,
                                 bg="white")
        self.left_image_label.image = self.left_image  # Keep a reference to the image
        self.left_image_label.pack(padx=45, pady=45)

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.175, rely=0.55)

        frame2 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame2.place(relx=0.4, rely=0.25)

        self.center_image = PhotoImage(file='Images/estate.png')
        self.center_image_label = Label(frame2,
                                   image=self.center_image,
                                   bg="white")
        self.center_image_label.image = self.center_image
        self.center_image_label.pack(padx=45, pady=45)

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.475, rely=0.55)

        frame3 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame3.place(relx=0.7, rely=0.25)

        # Adding image to the frame
        self.right_image = PhotoImage(file='Images/estate.png')
        self.right_image_label = Label(frame3,
                                  image=self.right_image,
                                  bg="white")
        self.right_image_label.image = self.right_image  # Keep a reference to the image
        self.right_image_label.pack(padx=45, pady=45)

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.775, rely=0.55)

        frame4 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE
                       )
        frame4.place(relx=0.1, rely=0.63)

        self.left_image = PhotoImage(file='Images/estate.png')
        left_image_label = Label(frame4,
                                 image=self.left_image,
                                 bg="white")
        left_image_label.image = self.left_image  # Keep a reference to the image
        left_image_label.pack(padx=45, pady=45)

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.175, rely=0.93)

        frame5 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame5.place(relx=0.4, rely=0.63)

        self.center_image = PhotoImage(file='Images/estate.png')
        center_image_label = Label(frame5,
                                   image=self.center_image,
                                   bg="white")
        center_image_label.image = self.center_image
        center_image_label.pack(padx=45, pady=45)

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.475, rely=0.93)

        frame6 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame6.place(relx=0.7, rely=0.63)

        self.right_image = PhotoImage(file='Images/estate.png')
        right_image_label = Label(frame6,
                                  image=self.right_image,
                                  bg="white")
        right_image_label.image = self.right_image  # Keep a reference to the image
        right_image_label.pack(padx=45, pady=45)

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.775, rely=0.93)

        # setting up the next page button

        prev_button = Button(root, bg='white', text='<<Prev',command = self.back)
        prev_button.place(relx=0.02, rely=0.5)

    def buy(self):
        self.root.destroy()
        import buy1
    def back(self):
        self.root.destroy()
        import maininterface
    def home(self):
        self.root.destroy()
        import maininterface
    def rent(self):
        self.root.destroy()
        import Rent1




root=Tk()
obj = maininterface2(root)
root.mainloop()

