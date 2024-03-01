from tkinter import *
from tkinter import ttk
import tkinter as tk


def create_main_window(parent, self=None):
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
    icon = PhotoImage(file='estate.png')
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




    #setting up view points of app
    frame1 = Frame(main_window,
                   width=800,
                   height=200,
                   bg="RED"
                   )
    frame1.pack( padx=10, pady=20,fill='x')

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="RED")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(side=LEFT,padx=30)

    info_label = Label(frame1, text="Some information goes here", font=("Arial", 12))
    info_label.pack(side=LEFT,padx=10)

    view_button = Button(frame1, text="View")
    view_button.pack(side=RIGHT,padx=10)

    #2
    frame1 = Frame(main_window,
                   width=800,
                   height=200,
                   bg="RED"
                   )
    frame1.pack(padx=10, pady=20,fill='x')

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="RED")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(side=LEFT, padx=30)

    info_label = Label(frame1, text="Some information goes here", font=("Arial", 12))
    info_label.pack(side=LEFT, padx=10)

    view_button = Button(frame1, text="View")
    view_button.pack(side=RIGHT, padx=10)

    #3
    frame1 = Frame(main_window,
                   width=800,
                   height=200,
                   bg="RED"
                   )
    frame1.pack(padx=10, pady=20,fill='x')

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="RED")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(side=LEFT, padx=30)

    info_label = Label(frame1, text="Some information goes here", font=("Arial", 12))
    info_label.pack(side=LEFT, padx=10)

    view_button = Button(frame1, text="View")
    view_button.pack(side=RIGHT, padx=10)

    #4
    frame1 = Frame(main_window,
                   width=800,
                   height=200,
                   bg="RED"
                   )
    frame1.pack(padx=10, pady=20,fill='x')

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="RED")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(side=LEFT, padx=30)

    info_label = Label(frame1, text="Some information goes here", font=("Arial", 12))
    info_label.pack(side=LEFT, padx=10)

    view_button = Button(frame1, text="View")
    view_button.pack(side=RIGHT, padx=10)

    #5
    frame1 = Frame(main_window,
                   width=800,
                   height=200,
                   bg="RED"
                   )
    frame1.pack(padx=10, pady=20,fill='x')

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="RED")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(side=LEFT, padx=30)

    info_label = Label(frame1, text="Some information goes here", font=("Arial", 12))
    info_label.pack(side=LEFT, padx=10)

    view_button = Button(frame1, text="View")
    view_button.pack(side=RIGHT, padx=10)

if __name__ == "__main__":
    window = Tk()
    create_main_window(window)
    window.mainloop()