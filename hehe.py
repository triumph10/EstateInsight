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
                relief=SUNKEN,
                bd=1,
                pady=3)
    one.grid(fill=X, row=0, column=0, sticky='n')
    insertButt = Button(one, text="Login", bg="#DFA878", border=0, activebackground='#B67352')
    insertButt.grid(sticky='ne', row=0, colmumn=0)
    insertButt = Button(one, text="Sign Up", bg="#DFA878", border=0, activebackground='#B67352')
    insertButt.grid(sticky='ne', row=0, column=0)

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

    main_window.grid_columnconfigure(0, weight=1, uniform="group1")
    main_window.grid_rowconfigure(0, weight=0)

    if __name__ == "__main__":
        window = Tk()
        create_main_window(window)
        window.mainloop()
