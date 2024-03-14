from tkinter import *
from tkinter import ttk
import tkinter as tk


class rent1:
    def __init__(self,root):
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
                    relief=SUNKEN,
                    bd=1,
                    pady=3)
        one.pack(fill=X, side=TOP)
        insertButt = Button(one, text="Login", bg="#B31312", fg='white', border=0, activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=3, pady=2)
        insertButt = Button(one, text="Sign Up", bg="#B31312", fg='white', border=0, activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=3, pady=2)

        # app color
        self.root.configure(bg='mintcream')

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
        toolbar = Frame(root, bg="MINTCREAM", relief=SUNKEN, bd=1, pady=2)
        printButt = Button(toolbar,
                           text="Home",
                           bg="white",
                           border=0,
                           activebackground='#B67352', command=self.home)
        printButt.pack(side=LEFT, padx=20, pady=2)
        insertButt = Button(toolbar, text="Buy", bg="WHITE", border=0, activebackground='#B67352',command = self.buy)
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Sell", bg="WHITE", border=0, activebackground='#B67352',command = self.sell)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Rent", bg="#B31312", border=1, relief=RAISED, fg='white',command = self.rent)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Wishlist", bg="WHITE", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Help", bg="WHITE", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

        frame = Frame(root, width=800, height=200, bg="white", bd=1, relief=GROOVE, highlightbackground='black',
                      highlightthickness=2)
        frame.pack(padx=10, pady=20, fill='x')

        self.left_image = PhotoImage(file='Images/estate.png')
        self.left_image_label = Label(frame, image=self.left_image, bg="white")
        self.left_image_label.image = self.left_image  # Keep a reference to the image
        self.left_image_label.pack(side=LEFT, padx=5)

        info_label = Label(frame, text=f"Korus Apt", font=("Arial", 12))
        info_label.pack(side=LEFT, padx=10)

        view_button = Button(frame, text="View", command=self.rentview)
        view_button.pack(side=RIGHT, padx=10)

        # setting up the next page button

        next_button = Button(root, bg='white', text='Next>>')
        next_button.place(relx=0.93, rely=0.93)

        # frame2
        frame = Frame(root, width=800, height=200, bg="white", bd=1, relief=GROOVE, highlightbackground='black',
                      highlightthickness=2)
        frame.pack(padx=10, pady=10, fill='x')

        self.left_image = PhotoImage(file='Images/estate.png')
        self.left_image_label = Label(frame, image=self.left_image, bg="white")
        self.left_image_label.image = self.left_image  # Keep a reference to the image
        self.left_image_label.pack(side=LEFT, padx=5)

        info_label = Label(frame, text=f"Random Property ", font=("Arial", 12))
        info_label.pack(side=LEFT, padx=10)

        view_button = Button(frame, text="View")
        view_button.pack(side=RIGHT, padx=10)

    def buy(self):
        self.root.destroy()
        import buy1
    def next(self):
        self.root.destroy()
        import maininterface2
    def home(self):
        self.root.destroy()
        import maininterface
    def rent(self):
        self.root.destroy()
        import Rent1
    def rentview(self):
        self.root.destroy()
        import Rent_View
    def sell(self):
        self.root.destroy()
        import sell


root=Tk()
obj = rent1(root)
root.mainloop()

