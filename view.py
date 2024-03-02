from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter import Image as ImageTk
import mysql.connector
import io


def fetch_data():
    # Connect to your MySQL database
    connection = mysql.connector.connect(
        host="local host",
        user="root",
        password="ARYA#305#varun",
        database="databasemain"
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Fetch image data
    cursor.execute("SELECT productimg FROM display WHERE productid = 12")
    productimg = cursor.fetchone()[0]

    # Fetch description data
    cursor.execute("SELECT description FROM display WHERE productid = 12")
    description = cursor.fetchone()[0]

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return productimg, description

def create_main_window(parent):
    main_window = Toplevel(parent)

    # setting up the app
    main_window.title("EstateInsight")
    main_window.resizable(False, False)

    font_info = ("Arial", 15, "bold")

    one = Label(main_window,
                text="EstateInsight",
                bg="#DFA878",
                fg="black",
                font=font_info,
                anchor=W,
                relief=SUNKEN,
                bd=1,
                pady=3)
    one.pack(fill=X, side=TOP)
    insertButt = Button(one, text="Login", bg="#DFA878", border=0, activebackground='#B67352')
    insertButt.pack(side=RIGHT, padx=3, pady=2)
    insertButt = Button(one, text="Sign Up", bg="#DFA878", border=0, activebackground='#B67352')
    insertButt.pack(side=RIGHT, padx=3, pady=2)

    # app color
    main_window.configure(bg='mintcream')



    # setting up geometry for app
    window_width = 1000
    window_height = 660

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    main_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # setting up icon for window title
    icon = PhotoImage(file='maininterfacechitresh/estate.png')
    main_window.iconphoto(True, icon)

    #setting up the toolbar for the app
    toolbar = Frame(main_window, bg="#DFA878", relief=SUNKEN, bd=1, pady=2)

    insertButt = Button(toolbar, text="Buy", bg="#DFA878", border=0, activebackground='#B67352')
    insertButt.pack(side=LEFT, padx=20, pady=2)
    printButt = Button(toolbar, text="Sell", bg="#DFA878", border=0, activebackground='#B67352')
    printButt.pack(side=LEFT, padx=20, pady=2)
    printButt = Button(toolbar, text="Rent", bg="#DFA878", border=0, activebackground='#B67352')
    printButt.pack(side=LEFT, padx=20, pady=2)
    printButt = Button(toolbar, text="Wishlist", bg="#DFA878", border=0,activebackground='#B67352')
    printButt.pack(side=LEFT, padx=20, pady=2)
    printButt = Button(toolbar, text="Help", bg="#DFA878", border=0, activebackground='#B67352')
    printButt.pack(side=LEFT, padx=20, pady=2)

    toolbar.pack(side=TOP, fill=X)

    # Add red boxes on the left and right for image and information
    image_frame = Frame(main_window, bg='red', width=300, height=500)
    image_frame.pack(side=LEFT, padx=10, pady=10)

    info_frame = Frame(main_window, bg='red', width=500, height=500)
    info_frame.place(relx=0.33, rely=0.5, anchor=CENTER)

    # Fetch data from the database
    image_data, description = fetch_data()

    # Convert the binary image data to a PhotoImage
    image = Image.open(io.BytesIO(image_data))
    image = ImageTk.PhotoImage(image)

    # Create a label to display the image in the left frame
    image_label = Label(image_frame, image=image, bg='red')
    image_label.image = image  # To prevent image from being garbage collected
    image_label.pack()

    # Create a label to display the description in the right frame
    description_label = Label(info_frame, text=description, bg='red', fg='white', font=('Arial', 12))
    description_label.pack()


if __name__ == "__main__":
    window = Tk()
    create_main_window(window)
    window.mainloop()