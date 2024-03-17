from tkinter import *
from tkinter import ttk
import tkinter as tk


class buy2:
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
                    relief=SUNKEN,
                    bd=1,
                    pady=3)
        one.pack(fill=X, side=TOP)
        name_label = Label(one,
                           text='Insert Name',
                           bg='#B31312',
                           fg='white',
                           bd=0)
        name_label.place(relx=0.85, rely=0.1)  # name
        down_arrow = Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
        down_arrow.pack()
        down_arrow.menu = Menu(down_arrow)
        down_arrow["menu"] = down_arrow.menu
        down_arrow.menu.add_checkbutton(label="Profile")
        down_arrow.menu.add_checkbutton(label="Agents")
        down_arrow.place(relx=0.92)  # drop down arrow

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
                           activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)

        insertButt = Button(toolbar, text="Buy", bg="#B31312", border=1, relief=RAISED, fg='white')
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Sell", bg="WHITE", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Rent", bg="WHITE", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Wishlist", bg="WHITE", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Help", bg="WHITE", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

        # Creating and packing frames inside the container
        for i in range(1, 11):
            frame = Frame(root, width=800, height=200, bg="white", bd=1, relief=GROOVE)
            frame.pack(padx=10, pady=20, fill='x', expand=True)

            left_image = PhotoImage(file='Images/estate.png')
            left_image_label = Label(frame, image=left_image, bg="white")
            left_image_label.image = left_image  # Keep a reference to the image
            left_image_label.pack(side=LEFT, padx=30)

            info_label = Label(frame, text=f"Some information goes here {i}", font=("Arial", 12))
            info_label.pack(side=LEFT, padx=10)

            view_button = Button(frame, text="View")
            view_button.pack(side=RIGHT, padx=10)

            # setting up the next page button

            next_button = Button(root, bg='white', text='<<Prev')
            next_button.place(relx=0.02, rely=0.93)




root=Tk()
obj = buy2(root)
root.mainloop()