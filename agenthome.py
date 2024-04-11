from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
from io import BytesIO
import matplotlib.pyplot as plt  # Importing matplotlib's pyplot module
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class agenthome:
    def  __init__(self, root, username):
        self.root = root
        self.username = username
        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)
        self.username = username  # this is used to store the username
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)
        font_info = ("Arial", 15, "bold")

        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ARYA#305#varun',
            database='estateinsight'
        )

        # Create a cursor to execute SQL queries
        self.cursor = self.conn.cursor()
        self.fetch_data_from_database()
        # Execute SELECT query to fetch name from the database table
        self.cursor.execute('SELECT username FROM signin WHERE username = %s', (self.username,))
        row = self.cursor.fetchone()
        if row:
            name = row[0]
        else:
            name = ""

        one = Label(root,
                    text="EstateInsight",
                    bg="#B31312",
                    fg="white",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=1,
                    height=1)
        one.pack(fill=X, side=TOP)
        name_label = Label(one,
                           text=self.username,
                           bg='#B31312',
                           fg='white',
                           bd=0, font=('Bold', 17))
        name_label.place(relx=0.78, rely=0.1, )  # name
        down_arrow = Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
        down_arrow.pack()
        down_arrow.menu = Menu(down_arrow)
        down_arrow["menu"] = down_arrow.menu
        down_arrow.menu.add_checkbutton(label="Profile", command=self.profile)
        down_arrow.menu.add_checkbutton(label="Agents", command=self.agent)
        down_arrow.place(relx=0.92)  # drop down arrow
        view_button = Button(root, text='View', bg="#B31312", fg="white", font=("Arial", 12), relief="raised",command=self.display_graph)
        view_button.place(relx=0.01, rely=0.55)
        # app color
        self.root.configure(bg='white')

        # setting up geometry for app
        window_width = 1000
        window_height = 680

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # setting up icon for window title
        self.icon = PhotoImage(file='Images/estate.png')
        self.root.iconphoto(True, self.icon)

        self.notification = self.fetch_notification()

        # Add label and button below the toolbar
        corner_frame = Frame(root, bg="red")
        corner_frame.place(x=700,y=100)

        # Add label
        # Add label to display notification
        corner_label = Label(corner_frame, text=self.notification, bg="red", fg='black')
        corner_label.pack(side=LEFT, padx=5)

        # Add button
        corner_button = Button(corner_frame, text="Accept Chat request", bg="#B31312",
                               fg="white",command=self.accept_chat_request)  # , command=self.corner_action)
        corner_button.pack(side=RIGHT, padx=4)

        # setting up the toolbar for the app
        toolbar = Frame(root, bg="white", relief=GROOVE, bd=2, pady=2)

        printButt = Button(toolbar,
                           text="Home",
                           bg="#B31312",
                           border=1,
                           relief=RAISED,
                           fg="white",
                           command=self.home)
        printButt.pack(side=LEFT, padx=20, pady=2)
        insertButt = Button(toolbar,
                            text="Buy",
                            bg="white",
                            border=0,
                            command=self.buy)
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Sell",
                           bg="white",

                           border=0,
                           activebackground='#B67352', command=self.sell)

        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Rent",
                           bg="white",

                           border=0, activebackground='#B67352', command=self.rent)

        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Wishlist",
                           bg="white",
                           border=0)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Help",
                           bg="white",
                           border=0)
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

        # setting up the search bar
        def on_enter(e):
            user.delete(0, 'end')

        def on_leave(e):
            name = user.get()
            if name == '':
                user.insert(0, 'Search')

        user = Entry(root,
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

        frame1 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       relief=GROOVE,
                       bd=1
                       )
        frame1 = Frame(root, width=200, height=200, bg="white")
        frame1.place(relx=0.1, rely=0.25)

        # Fetch image from database and display
        self.display_image_from_database(frame1, 1)  # Assuming image ID 1

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.2, rely=0.55)

        frame2 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame2.place(relx=0.4, rely=0.25)

        # Fetch image from database and display
        self.display_image_from_database(frame2, 2)  # Assuming image ID 2

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.5, rely=0.55)

        frame3 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame3.place(relx=0.7, rely=0.25)

        # Fetch image from database and display
        self.display_image_from_database(frame3, 3)  # Assuming image ID 3

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.8, rely=0.55)

        frame4 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE
                       )
        frame4.place(relx=0.1, rely=0.63)

        # Fetch image from database and display
        self.display_image_from_database(frame4, 4)  # Assuming image ID 4

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.2, rely=0.93)

        frame5 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame5.place(relx=0.4, rely=0.63)

        # Fetch image from database and display
        self.display_image_from_database(frame5, 5)  # Assuming image ID 5

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.5, rely=0.93)

        frame6 = Frame(root,
                       width=200,
                       height=200,
                       bg="white",
                       bd=1,
                       relief=GROOVE)
        frame6.place(relx=0.7, rely=0.63)

        # Fetch image from database and display
        self.display_image_from_database(frame6, 6)  # Assuming image ID 6

        view_butt = Button(root, bg='white', bd=1, text='View')
        view_butt.place(relx=0.8, rely=0.93)

    def fetch_data_from_database(self):
        try:
            # Execute SELECT query to fetch dates and prices from the database
            self.cursor.execute("SELECT date, price FROM mumbai_pd")

            # Fetch all rows
            rows = self.cursor.fetchall()

            # Extract dates and prices from the fetched rows
            self.dates = [row[0] for row in rows]
            self.prices = [row[1] for row in rows]

        except mysql.connector.Error as e:
            print("Error fetching data from MySQL:", e)

    def display_graph(self):
        try:
            # Plot the graph using matplotlib
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.plot(self.dates, self.prices, marker='o', linestyle='-')
            ax.set_title('Price Trends Over Time')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price ($)')
            ax.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()

            # Create a new window to display the graph
            graph_window = Toplevel(self.root)
            graph_window.title("Price Trends Graph")
            graph_window.geometry("800x600")

            # Convert plot to a Tkinter-compatible photo image
            graph_photo = FigureCanvasTkAgg(fig, master=graph_window)
            graph_photo.draw()
            graph_photo.get_tk_widget().pack()

        except Exception as e:
            print("Error displaying graph:", e)
    def buy(self):
        self.root.destroy()
        import buy1

    def agent(self):
        self.root.destroy()
        import Agent1

    def profile(self):
        self.root.destroy()
        import Profile

    def next(self):
        self.root.destroy()
        import Homepage2

    def home(self):
        self.root.destroy()
        import Homepage2

    def rent(self):
        self.root.destroy()
        import Rent1

    def sell(self):
        self.root.destroy()
        import Sell_1

    def fetch_notification(self):
        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='ARYA#305#varun',
                database='estateinsight'
            )

            # Create a cursor to execute SQL queries
            cursor = conn.cursor()

            # Execute SELECT query to fetch notification from the agent table
            cursor.execute("SELECT notification FROM agent WHERE username = %s", (self.username,))
            row = cursor.fetchone()

            if row:
                return row[0]
            else:
                return "No notification available"  # Provide a default message if no notification found

        except mysql.connector.Error as e:
            print("Error fetching notification:", e)

    def accept_chat_request(self):
        import chat
        try:
            # Connect to the database
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='ARYA#305#varun',
                database='estateinsight'
            )

            # Create a cursor to execute SQL queries
            cursor = conn.cursor()

            # Execute DELETE query to remove the notification from the agent table
            cursor.execute("UPDATE agent SET notification = NULL WHERE username = %s", (self.username,))
            conn.commit()  # Commit the transaction

            print("Notification deleted successfully")

        except mysql.connector.Error as e:
            print("Error deleting notification:", e)


    def display_image_from_database(self, frame, image_id):
        try:
            cursor = self.conn.cursor()
            # Fetch image data from the database
            cursor.execute("SELECT photo1 FROM estate_data WHERE ID = %s", (image_id,))
            image_data = cursor.fetchone()
            if image_data:
                image_data = image_data[0]  # Extract image data from the tuple

                # Convert binary image data to Image object
                image = Image.open(image_data)

                # Resize image
                image.thumbnail((200, 200))

                # Convert Image object to PhotoImage object
                photo_image = ImageTk.PhotoImage(image)

                # Display image in label
                label = Label(frame, image=photo_image, bg="white")
                label.image = photo_image  # Keep a reference to the image
                label.pack(padx=45, pady=45)
            else:
                print("No image data found for image ID:", image_id)

        except Exception as e:
            print("Error displaying image:", e)


root = Tk()
obj = agenthome(root, "")
root.mainloop()