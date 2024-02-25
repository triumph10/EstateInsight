from tkinter import *
import tkinter as tk
from maininterface import create_main_window

# Setting Up the app
window = Tk()
window.title("EstateInsight")
window.title("EstateInsight")

# Setting up the position of the app
window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Setting up the appearance
window.configure(background="#219ebc")

# Setting up the icon for the window
icon = PhotoImage(file='estate.png')
window.iconphoto(True, icon)

# Setting up the font
font_moodlift = ('Arial', 30, 'bold')
font_welcome = ("Arial", 15, "bold")
font_info = ("Arial", 15, "bold")
font_button = ("Arial", 10, "bold")

# Setting up the intro for the image label
photo = PhotoImage(file='estate.png')
language_language_label = Label(window,
                                text="EstateInsight",
                                font=font_moodlift,
                                fg='#FFFFFF',
                                bg='#219ebc',
                                image=photo,  # replaces the text with image label
                                compound='top')
language_language_label.pack(padx=10, pady=20)

# Setting up the label for the welcome text
welcome_label = Label(window,
                      text="Welcome To",
                      font=font_welcome,
                      fg='#FFFFFF',
                      bg='#219ebc')

welcome_label.pack(padx=5, pady=5)

# Setting up the Label For information
infoLabel = tk.Label(window,
                     text="The Real Estate Discovery Platform",
                     fg='#FFFFFF',
                     bg='#219ebc',
                     font=font_info)
infoLabel.pack()


# Setting up the entry button

def new_window():
    window.withdraw()  # Hide the main window
    main_window = create_main_window(window)
    main_window.protocol("WM_DELETE_WINDOW", lambda: close_windows(window, main_window))


def close_windows(main_window, popup_window):
    popup_window.destroy()
    main_window.destroy()


Entry = Button(window,
               text="Get Started",
               foreground='#E4DEBE',
               background='#86A7FC',
               activeforeground='#D24545',
               activebackground='#3468C0',
               command=new_window,
               font=font_button
               )
Entry.pack(padx=10, pady=20)

window.mainloop()
