from tkinter import *
from tkinter import ttk
import tkinter as tk


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
                relief=GROOVE,
                bd=1,
                height=5)
    one.pack(fill=X, side=TOP)
    insertButt = Button(one,
                        text="Login",
                        bg="#DFA878",
                        border=0,
                        activebackground='#B67352')
    insertButt.pack(side=RIGHT, padx=3, pady=2)
    insertButt = Button(one,
                        text="Sign Up",
                        bg="#DFA878",
                        border=0,
                        activebackground='#B67352')
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
    toolbar = Frame(main_window, bg="#DFA878", relief=GROOVE, bd=1, pady=2)

    insertButt = Button(toolbar,
                        text="Buy",
                        bg="#DFA878",
                        border=0,
                        activebackground='#B67352')
    insertButt.pack(side=LEFT, padx=20, pady=2)
    printButt = Button(toolbar,
                       text="Sell",
                       bg="#DFA878",
                       border=0,
                       activebackground='#B67352')
    printButt.pack(side=LEFT, padx=20, pady=2)
    printButt = Button(toolbar,
                       text="Rent",
                       bg="#DFA878",
                       border=0,
                       activebackground='#B67352')
    printButt.pack(side=LEFT, padx=20, pady=2)
    printButt = Button(toolbar,
                       text="Wishlist",
                       bg="#DFA878",
                       border=0,
                       activebackground='#B67352')
    printButt.pack(side=LEFT, padx=20, pady=2)
    printButt = Button(toolbar,
                       text="Help",
                       bg="#DFA878",
                       border=0,
                       activebackground='#B67352')
    printButt.pack(side=LEFT, padx=20, pady=2)

    toolbar.pack(side=TOP, fill=X)

    #Creating a scroll bar for the app

    # my_canvas = Canvas(main_frame)
    # my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #
    # my_scrollbar = ttk.Scrollbar(main_frame,
    #                              orient=VERTICAL,
    #                              command=my_canvas.yview)
    # my_scrollbar.pack(side=RIGHT, fill=Y)
    #
    # my_canvas.configure(yscrollcommand=my_scrollbar.set)
    # my_canvas.bind('<Configure>',
    #                lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    #
    # second_frame = Frame(my_canvas)
    #
    # my_canvas.create_window((0,0), window=second_frame,
    #                                anchor='nw')

    #setting up the search bar
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, 'Search')

    user = Entry(main_window,
                 width=25,
                 fg='black',
                 border=0,
                 bg="white",
                 relief=RAISED,
                 font=('Microsoft YaHei UI Light', 11))
    user.place(x=400, y=100)
    user.insert(0, "Search")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(main_window, width=203, height=2, bg='black').place(x=400, y=125)

    #setting up view points of app
    frame1 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD"
                   )
    frame1.place(relx=0.1, rely=0.25)

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame1,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(padx=45, pady=45)

    view_butt = Button(main_window, bg='#DFA878', text='View')
    view_butt.place(relx=0.175, rely=0.55)

    frame2 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame2.place(relx=0.4, rely=0.25)

    center_image = PhotoImage(file='estate.png')
    center_image_label = Label(frame2,
                               image=center_image,
                               bg="#3652AD")
    center_image_label.image = center_image
    center_image_label.pack(padx=45, pady=45)

    view_butt = Button(main_window, bg='#DFA878', text='View')
    view_butt.place(relx=0.475, rely=0.55)

    frame3 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#DFA878")
    frame3.place(relx=0.7, rely=0.25)

    # Adding image to the frame
    right_image = PhotoImage(file='estate.png')
    right_image_label = Label(frame3,
                              image=right_image,
                              bg="#DFA878")
    right_image_label.image = right_image  # Keep a reference to the image
    right_image_label.pack(padx=45, pady=45)

    view_butt = Button(main_window, bg='#DFA878', text='View')
    view_butt.place(relx=0.775, rely=0.55)

    frame4 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD"
                   )
    frame4.place(relx=0.1, rely=0.63)

    left_image = PhotoImage(file='estate.png')
    left_image_label = Label(frame4,
                             image=left_image,
                             bg="#3652AD")
    left_image_label.image = left_image  # Keep a reference to the image
    left_image_label.pack(padx=45, pady=45)

    view_butt = Button(main_window, bg='#DFA878', text='View')
    view_butt.place(relx=0.175, rely=0.93)

    frame5 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#3652AD")
    frame5.place(relx=0.4, rely=0.63)

    center_image = PhotoImage(file='estate.png')
    center_image_label = Label(frame5,
                               image=center_image,
                               bg="#3652AD")
    center_image_label.image = center_image
    center_image_label.pack(padx=45, pady=45)

    view_butt = Button(main_window, bg='#DFA878',  text='View')
    view_butt.place(relx=0.475, rely=0.93)

    frame6 = Frame(main_window,
                   width=200,
                   height=200,
                   bg="#DFA878")
    frame6.place(relx=0.7, rely=0.63)

    right_image = PhotoImage(file='estate.png')
    right_image_label = Label(frame6,
                              image=right_image,
                              bg="#DFA878")
    right_image_label.image = right_image  # Keep a reference to the image
    right_image_label.pack(padx=45, pady=45)

    view_butt = Button(main_window, bg='#DFA878', text='View')
    view_butt.place(relx=0.775, rely=0.93)

    #setting up the next page button

    next_button = Button(main_window, bg='#DFA878', text='Next>>')
    next_button.place(relx=0.93, rely=0.5)




if __name__ == "__main__":
    window = Tk()
    create_main_window(window)
    window.mainloop()
