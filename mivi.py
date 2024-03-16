from tkinter import *
from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt  # Importing matplotlib's pyplot module
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class maininterface:
    def __init__(self, root):
        self.root = root
        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 20, "bold")  # Increased font size

        one = Label(root,
                    text="EstateInsight",
                    bg="#B31312",
                    fg="white",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=2,  # Increased border width
                    height=7)  # Increased height
        one.pack(fill=X, side=TOP)

        insertButt = Button(one,
                            text="Login",
                            bg="#B31312",
                            fg="white",
                            border=0,
                            activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=5, pady=5)  # Increased padding
        insertButt = Button(one,
                            text="Sign Up",
                            bg="#B31312",
                            fg="white",
                            border=0,
                            activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=5, pady=5)  # Increased padding

        # app color
        self.root.configure(bg='mintcream')

        # setting up geometry for app
        window_width = 1500  # Increased window width
        window_height = 1080  # Increased window height

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # setting up icon for window title
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)

        # setting up the toolbar for the app
        toolbar = Frame(root, bg="white", relief=GROOVE, bd=2, pady=5)  # Increased border width and padding

        printButt = Button(toolbar,
                           text="Home",
                           bg="white",
                           border=0,
                           activebackground='#B67352', command=self.home)
        printButt.pack(side=LEFT, padx=30, pady=5)  # Increased padding
        insertButt = Button(toolbar,
                            text="Buy",
                            bg="white",
                            border=0,
                            command=self.buy)
        insertButt.pack(side=LEFT, padx=30, pady=5)  # Increased padding
        printButt = Button(toolbar,
                           text="Sell",
                           bg="white",
                           border=0)
        printButt.pack(side=LEFT, padx=30, pady=5)  # Increased padding
        printButt = Button(toolbar,
                           text="Rent",
                           bg="white",
                           border=0,
                           activebackground='#B67352', command=self.rent)
        printButt.pack(side=LEFT, padx=30, pady=5)  # Increased padding
        printButt = Button(toolbar,
                           text="Wishlist",
                           bg="white",
                           border=0)
        printButt.pack(side=LEFT, padx=30, pady=5)  # Increased padding
        printButt = Button(toolbar,
                           text="Help",
                           bg="white",
                           border=0)
        printButt.pack(side=LEFT, padx=30, pady=5)  # Increased padding

        toolbar.pack(side=TOP, fill=X)

        # setting up the search bar
        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Search')

        user = Entry(root,
                     width=30,  # Increased width
                     fg='black',
                     bg="white",
                     relief=GROOVE,
                     font=('Arial', 15))  # Increased font size
        user.place(x=500, y=120)  # Adjusted position
        user.insert(0, "Search")
        user.bind('<FocusIn>', on_enter)
        user.bind('<FocusOut>', on_leave)

        Frame(root, width=303, height=3, bg='black').place(x=500, y=160)  # Increased width

        # setting up view points of app

        frame3 = Frame(root,
                       width=300,
                       height=300,
                       bg="white",
                       bd=2,
                       relief=GROOVE)  # Increased border width
        frame3.place(relx=0.7, rely=0.25)

        # Adding image to the frame
        right_image = PhotoImage(file='Images/estate.png')
        right_image_label = Label(frame3,
                                  image=right_image,
                                  bg="white")
        right_image_label.image = right_image  # Keep a reference to the image
        right_image_label.pack(padx=70, pady=70)  # Increased padding

        view_butt = Button(root, bg='white', bd=2, text='View')  # Increased border width
        view_butt.place(relx=0.775, rely=0.55)

        frame4 = Frame(root,
                       width=800,  # Increased width
                       height=600,  # Increased height
                       bg="red",
                       bd=2,
                       relief=GROOVE
                       )
        frame4.place(relx=0.05, rely=0.24)

        # Matplotlib graph
        dates = pd.date_range('2023-01-01', periods=12, freq='M')
        prices = [300000, 305000, 310000, 315000, 320000, 325000, 330000, 335000, 340000, 345000, 350000, 355000]
        df = pd.DataFrame({'Date': dates, 'Price': prices})

        fig, ax = plt.subplots(figsize=(8, 6))  # Adjust the figsize to fit inside frame4
        ax.plot(df['Date'], df['Price'], marker='o', linestyle='-')
        ax.set_title('Price Trends Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price ($)')
        ax.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Convert plot to a Tkinter-compatible photo image
        canvas = FigureCanvasTkAgg(fig, master=frame4)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP)

        frame6 = Frame(root,
                       width=300,
                       height=300,
                       bg="white",
                       bd=2,
                       relief=GROOVE)
        frame6.place(relx=0.7, rely=0.63)

        right_image = PhotoImage(file='Images/estate.png')
        right_image_label = Label(frame6,
                                  image=right_image,
                                  bg="white")
        right_image_label.image = right_image  # Keep a reference to the image
        right_image_label.pack(padx=70, pady=70)

        view_butt = Button(root, bg='white', bd=2, text='View')
        view_butt.place(relx=0.775, rely=0.93)

        # setting up the next page button
        next_button = Button(root, bg='white', text='Next>>', command=self.next)
        next_button.place(relx=0.93, rely=0.5)

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


root=Tk()
obj = maininterface(root)
root.mainloop()

