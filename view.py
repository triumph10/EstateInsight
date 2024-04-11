from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import io
import tkintermapview
import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime


class view:
    def __init__(self, root):
        self.root = root
        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 15, "bold")

        one = Label(root,
                    text="EstateInsight",
                    bg="RED",
                    fg="White",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=1,
                    pady=3)
        one.pack(fill=X, side=TOP)
        insertButt = Button(one, text="Login", bg="RED", border=0, activebackground='White')
        insertButt.pack(side=RIGHT, padx=3, pady=2)
        insertButt = Button(one, text="Sign Up", bg="RED", border=0, activebackground='White')
        insertButt.pack(side=RIGHT, padx=3, pady=2)
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='ARYA#305#varun',
                database='estateinsight'
            )
            self.cursor = self.conn.cursor()
            print("Connected to MySQL")
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Database Error", "Failed to connect to database")
            return
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
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)

        # setting up the toolbar for the app
        toolbar = Frame(root, bg="WHite", relief=SUNKEN, bd=1, pady=2)

        insertButt = Button(toolbar, text="Buy", bg="White", border=0, activebackground='#B67352')
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Sell", bg="White", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Rent", bg="White", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Wishlist", bg="White", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar, text="Help", bg="White", border=0, activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)
        # ------------------------------------------------------------------------------------------------------------------
        frame1 = Frame(root, width=100, height=10, bg="white", bd=1, relief=GROOVE)
        frame1.place(relx=0, rely=0.25)

        # Create a frame for date and price entry fields
        entry_frame = Frame(root, bg="red")
        entry_frame.place(x=50, y=120)
        # Create a label for the city
        city_label = Label(root, text="Mumbai", font=("Arial", 18, "bold"), bg="mintcream")
        city_label.place(x=50, y=70)
        # Entry fields for date and price
        date_label = Label(entry_frame, text="Date:", font=("Arial", 12), bg="mintcream")
        date_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Add a DateEntry widget for selecting dates
        self.calendar_frame = Frame(entry_frame, bg="mintcream")
        self.calendar_frame.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.date_entry = DateEntry(self.calendar_frame, width=12, background='darkblue',
                                    foreground='white', borderwidth=2)
        self.date_entry.pack()

        price_label = Label(entry_frame, text="Price:", font=("Arial", 12), bg="mintcream")
        price_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.price_entry = Entry(entry_frame, font=("Arial", 12), bd=2)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Button to submit the input
        submit_button = Button(root, text="Submit", command=self.submit_input, bg="RED", fg="White", bd=2,
                               font=("Arial", 12))
        submit_button.place(x=200, y=200)
        # ----------------------------------------------------------------------------------------------------------------------------
        # frame2 = Frame(root, width=100, height=10, bg="white", bd=1, relief=GROOVE)
        # frame2.place(relx=3, rely=0.25)

        # Create a frame for date and price entry fields
        entry_frame1 = Frame(root, bg="red")
        entry_frame1.place(x=600, y=120)
        # Create a label for the city
        city_label1 = Label(root, text="Delhi", font=("Arial", 18, "bold"), bg="mintcream")
        city_label1.place(x=600, y=70)
        # Entry fields for date and price
        date_label1 = Label(entry_frame1, text="Date:", font=("Arial", 12), bg="mintcream")
        date_label1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Add a DateEntry widget for selecting dates
        self.calendar_frame1 = Frame(entry_frame1, bg="mintcream")
        self.calendar_frame1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.date_entry1 = DateEntry(self.calendar_frame1, width=12, background='darkblue',
                                     foreground='white', borderwidth=2)
        self.date_entry1.pack()

        price_label1 = Label(entry_frame1, text="Price:", font=("Arial", 12), bg="mintcream")
        price_label1.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.price_entry1 = Entry(entry_frame1, font=("Arial", 12), bd=2)
        self.price_entry1.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Button to submit the input
        submit_button2 = Button(root, text="Submit", command=self.submit_input2, bg="RED", fg="White", bd=2,
                                font=("Arial", 12))
        submit_button2.place(x=600, y=200)

    # ---------------------------------------------------------------------------------------------------------------------------
        entry_frame2 = Frame(root, bg="red")
        entry_frame2.place(x=50, y=320)
        # Create a label for the city
        city_label2= Label(root, text="Bengaluru", font=("Arial", 18, "bold"), bg="mintcream")
        city_label2.place(x=50, y=280)
        # Entry fields for date and price
        date_label2 = Label(entry_frame2, text="Date:", font=("Arial", 12), bg="mintcream")
        date_label2.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Add a DateEntry widget for selecting dates
        self.calendar_frame2 = Frame(entry_frame2, bg="mintcream")
        self.calendar_frame2.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.date_entry2 = DateEntry(self.calendar_frame2, width=12, background='darkblue',
                                     foreground='white', borderwidth=2)
        self.date_entry2.pack()

        price_label2 = Label(entry_frame2, text="Price:", font=("Arial", 12), bg="mintcream")
        price_label2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.price_entry2 = Entry(entry_frame2, font=("Arial", 12), bd=2)
        self.price_entry2.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Button to submit the input
        submit_button3 = Button(root, text="Submit", command=self.submit_input, bg="RED", fg="White", bd=2,
                                font=("Arial", 12))
        submit_button3.place(x=50, y=400)
#--------------------------------------------------------------------------------------------------------------------
        entry_frame3 = Frame(root, bg="red")
        entry_frame3.place(x=600, y=320)
        # Create a label for the city
        city_label3 = Label(root, text="Chennai", font=("Arial", 18, "bold"), bg="mintcream")
        city_label3.place(x=600, y=280)
        # Entry fields for date and price
        date_label3 = Label(entry_frame3, text="Date:", font=("Arial", 12), bg="mintcream")
        date_label3.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        # Add a DateEntry widget for selecting dates
        self.calendar_frame3 = Frame(entry_frame3, bg="mintcream")
        self.calendar_frame3.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.date_entry3 = DateEntry(self.calendar_frame3, width=12, background='darkblue',
                                     foreground='white', borderwidth=2)
        self.date_entry3.pack()

        price_label3 = Label(entry_frame3, text="Price:", font=("Arial", 12), bg="mintcream")
        price_label3.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.price_entry3 = Entry(entry_frame3, font=("Arial", 12), bd=2)
        self.price_entry3.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Button to submit the input
        submit_button4 = Button(root, text="Submit", command=self.submit_input, bg="RED", fg="White", bd=2,
                                font=("Arial", 12))
        submit_button4.place(x=600, y=400)
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
    def submit_input(self):
        # Get the input values
        selected_date = self.date_entry.get()
        price = self.price_entry.get()

        try:
            # Convert the selected date to the correct format
            formatted_date = datetime.strptime(selected_date, "%m/%d/%y").strftime("%Y-%m-%d")

            # Execute an INSERT query to save the input values to the database
            sql = "INSERT INTO mumbai_pd (date, price) VALUES (%s, %s)"
            values = (formatted_date, price)
            self.cursor.execute(sql, values)

            # Commit the transaction
            self.conn.commit()

            print("Input values saved to database successfully.")

        except mysql.connector.Error as e:
            # Roll back the transaction in case of an error
            self.conn.rollback()
            print("Error saving input values to database:", e)
#-------------------------------------------------------------------------------------------------------------------------
    def submit_input2(self):
        # Get the input values
        selected_date2 = self.date_entry.get()
        price2 = self.price_entry1.get()

        if not price2:
            messagebox.showerror("Input Error", "Price field cannot be empty.")
            return

        try:
            # Convert the selected date to the correct format
            formatted_date2 = datetime.strptime(selected_date2, "%m/%d/%y").strftime("%Y-%m-%d")

            # Execute an INSERT query to save the input values to the database
            sql2 = "INSERT INTO delhi_pd (date, price) VALUES (%s, %s)"
            values2 = (formatted_date2, price2)
            self.cursor.execute(sql2, values2)

            # Commit the transaction
            self.conn.commit()

            print("Input values saved to database successfully.")

        except mysql.connector.Error as e:
            # Roll back the transaction in case of an error
            self.conn.rollback()
            print("Error saving input values to database:", e)
#-------------------------------------------------------------------------------------------------------
    def submit_input3(self):
        # Get the input values
        selected_date3 = self.date_entry2.get()
        price3 = self.price_entry2.get()

        try:
            # Convert the selected date to the correct format
            formatted_date3 = datetime.strptime(selected_date3, "%m/%d/%y").strftime("%Y-%m-%d")

            # Execute an INSERT query to save the input values to the database
            sql3 = "INSERT INTO bengaluru_pd (date, pice) VALUES (%s, %s)"
            values3 = (formatted_date3, price3)
            self.cursor.execute(sql3, values3)

            # Commit the transaction
            self.conn.commit()

            print("Input values saved to database successfully.")

        except mysql.connector.Error as e:
            # Roll back the transaction in case of an error
            self.conn.rollback()
            print("Error saving input values to database:", e)


root = Tk()
obj = view(root)
root.mainloop()