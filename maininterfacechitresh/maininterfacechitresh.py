from tkinter import *
from tkinter import ttk


def create_main_window(parent):
    main_window = Toplevel(parent)

    # setting up the app
    main_window.title("EstateInsight")
    main_window.resizable(False, False)

    font_info = ("Arial", 15, "bold")

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

    one = Label(main_window,
                text="EstateInsight",
                bg="#DFA878",
                fg="black",
                font=font_info,
                anchor=W,
                relief=SUNKEN,
                bd=1,
                pady=3)
    one.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

    loginbutton = Button(main_window, text="Login", bg="#DFA878", border=0, activebackground='#B67352')
    loginbutton.grid(row=0, column=0, columnspan=3, padx=(10, 200), pady=12, sticky='ne')

    signupbutton = Button(main_window, text="Signup", bg="#DFA878", border=0, activebackground='#B67352')
    signupbutton.grid(row=0, column=0, columnspan=3, padx=(10, 100), pady=12, sticky='ne')

    # setting up the toolbar for the app
    toolbar = Frame(main_window, bg="#DFA878", relief=SUNKEN, bd=1, pady=2, height=4)

    insertButt = Button(toolbar, text="Buy", bg="#DFA878", border=0, activebackground='#B67352')
    insertButt.grid(row=1, column=0, columnspan=3, padx=(10, 100), pady=10, sticky='w')

    printButt = Button(toolbar, text="Sell", bg="#DFA878", border=0, activebackground='#B67352')
    printButt.grid(row=1, column=0, columnspan=3, padx=(200,10), pady=10, sticky='w')

    printButt = Button(toolbar, text="Rent", bg="#DFA878", border=0, activebackground='#B67352')
    printButt.grid(row=1, column=0, columnspan=3, padx=(400,10), pady=10, sticky='w')

    printButt = Button(toolbar, text="Wishlist", bg="#DFA878", border=0, activebackground='#B67352')
    printButt.grid(row=1, column=0, columnspan=3, padx=(600, 10), pady=10, sticky='w')

    printButt = Button(toolbar, text="Help", bg="#DFA878", border=0, activebackground='#B67352')
    printButt.grid(row=1, column=0, columnspan=3, padx=(800, 10), pady=10, sticky='w')

    toolbar.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

    # # Creating a scroll bar for the app
    #  main_frame = Frame(main_window)
    #  main_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky='nswe')
    #
    #  my_canvas = Canvas(main_frame)
    #  my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #
    #  my_scrollbar = ttk.Scrollbar(main_frame,
    #                               orient=VERTICAL,
    #                               command=my_canvas.yview)
    #  my_scrollbar.pack(side=RIGHT, fill=Y)
    #
    #  my_canvas.configure(yscrollcommand=my_scrollbar.set)
    #  my_canvas.bind('<Configure>',
    #                 lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    #
    #  second_frame = Frame(my_canvas)
    #
    #  my_canvas.create_window((0, 0), window=second_frame,
    #                          anchor='nw')

    # setting up the search bar
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Search')

    user = Entry(main_window, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=380, y=120)
    user.insert(0, "Search")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(main_window, width=203, height=2, bg='black').place(x=380, y=145)

    # setting up view points of app
    frame1 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD"
                   )
    frame1.grid(row=2, column=0, padx=10, pady=50)

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.grid(padx=45, pady=45)

    frame2 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame2.grid(row=2, column=1, padx=10, pady=50)

    center_image = PhotoImage(file='estate.png')
    center_image_label = Label(frame2,
                               image=center_image,
                               bg="#3652AD")
    center_image_label.image = center_image
    center_image_label.grid(padx=45, pady=45)

    frame3 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame3.grid(row=2, column=2, padx=10, pady=50)

    # Adding image to the frame
    right_image = PhotoImage(file='estate.png')
    right_image_label = Label(frame3,
                              image=right_image,
                              bg="#3652AD")
    right_image_label.image = right_image  # Keep a reference to the image
    right_image_label.grid(padx=45, pady=45)

    frame1 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD"
                   )
    frame1.grid(row=3, column=0, padx=10, pady=50)

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.grid(padx=45, pady=45)

    frame2 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame2.grid(row=3, column=1, padx=10, pady=50)

    center_image = PhotoImage(file='estate.png')
    center_image_label = Label(frame2,
                               image=center_image,
                               bg="#3652AD")
    center_image_label.image = center_image
    center_image_label.grid(padx=45, pady=45)

    frame3 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame3.grid(row=3, column=2, padx=10, pady=50)

    # Adding image to the frame
    right_image = PhotoImage(file='estate.png')
    right_image_label = Label(frame3,
                              image=right_image,
                              bg="#3652AD")
    right_image_label.image = right_image  # Keep a reference to the image
    right_image_label.grid(padx=45, pady=45)


    # Configure column sizes
    main_window.grid_columnconfigure(0, weight=1, uniform="group1")
    main_window.grid_columnconfigure(1, weight=1, uniform="group1")
    main_window.grid_columnconfigure(2, weight=1, uniform="group1")

    # Configure row sizes
    main_window.grid_rowconfigure(0, weight=0)
    main_window.grid_rowconfigure(1, weight=0)
    main_window.grid_rowconfigure(2, weight=0)
    main_window.grid_rowconfigure(3, weight=0)
    main_window.grid_rowconfigure(4, weight=0)
    main_window.grid_rowconfigure(5, weight=0)
    main_window.grid_rowconfigure(6, weight=0)
    main_window.grid_rowconfigure(7, weight=0)


if __name__ == "__main__":
    window = Tk()
    create_main_window(window)
    window.mainloop()
