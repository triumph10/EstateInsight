from tkinter import *
from tkinter import ttk
import tkinter as tk

def on_canvas_configure(event, canvas=None):
    canvas.configure(scrollregion=canvas.bbox("all"))
def create_main_window(parent, self=None, on_canvas_configure=None):
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

    main_frame = Frame(main_window)
    main_frame.pack(fill=BOTH, expand=1)

    # my_canvas = Canvas(main_frame)
    # my_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    #
    # my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    # my_scrollbar.pack(side=RIGHT, fill=Y)
    #
    # my_canvas.configure(yscrollcommand=my_scrollbar.set)
    # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    #
    # second_frame = Frame(my_canvas)
    #
    # my_canvas.create_window((0, 0), window=second_frame, anchor='center')
    canvas = tk.Canvas(main_window, bg='mintcream', scrollregion=(0, 0, 2000, 5000))
    canvas.pack(expand=True, fill='both')

    scrollbar = ttk.Scrollbar(main_window, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.place(relx=1, rely=0.1, relheight=1, anchor='ne')
    canvas.bind('<Configure>', on_canvas_configure)

    # Creating and packing frames inside the container
    for i in range(1, 11):
        frame = Frame(canvas, width=800, height=200, bg="RED")
        frame.pack(padx=10, pady=20, fill='x',expand=True)

        left_image = PhotoImage(file='estate.png')
        left_image_label = Label(frame, image=left_image, bg="RED")
        left_image_label.image = left_image  # Keep a reference to the image
        left_image_label.pack(side=LEFT, padx=30)

        info_label = Label(frame, text=f"Some information goes here {i}", font=("Arial", 12))
        info_label.pack(side=LEFT, padx=10)

        view_button = Button(frame, text="View")
        view_button.pack(side=RIGHT, padx=10)

        canvas.create_window(0, i * 220, window=frame, anchor='nw')

    main_window.mainloop()


if __name__ == "_main_":
    window = Tk()
    create_main_window(window)
    window.mainloop()