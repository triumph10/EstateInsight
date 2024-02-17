from tkinter import *
import tkinter as tk


def create_main_window(parent):
    main_window = Toplevel(parent)
    # setting up the app
    main_window.title("EstateInsight")
    main_window.resizable(False, False)

    font_info = ("Arial", 15, "bold")

    one = Label(main_window,
                text="EstateInsight",
                bg="#219ebc",
                fg="mintcream",
                font=font_info)
    one.pack(fill=X, side=TOP)

    # app color
    main_window.configure(bg='#219ebc')



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


if __name__ == "__main__":
    window = Tk()
    create_main_window(window)
    window.mainloop()
