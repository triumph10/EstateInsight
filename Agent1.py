from tkinter import *
from tkinter import ttk
import tkinter as tk

main_window = Tk()


# def create_main_window(parent, self=None, on_canvas_configure=None):
#     main_window = Toplevel(parent)

    # setting up the app
main_window.title("EstateInsight")
main_window.resizable(False, False)

font_info = ("Arial", 15, "bold")

one = Label(main_window,
                text="EstateInsight",
                bg="#B31312",
                fg="white",
                font=font_info,
                anchor=W,
                relief=SUNKEN,
                bd=1,
                pady=3)
one.pack(fill=X, side=TOP)
insertButt = Button(one, text="Login", bg="#B31312", fg='white', border=0, activebackground='#B67352')
insertButt.pack(side=RIGHT, padx=3, pady=2)
insertButt = Button(one, text="Sign Up", bg="#B31312", fg='white', border=0, activebackground='#B67352')
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
icon = PhotoImage(file='Images/estate.png')
main_window.iconphoto(True, icon)

#setting up the main widgets

frame1 = Frame(main_window, width=800, height=200, bg="white", bd=1, relief=GROOVE)
# frame1.pack(padx=10, pady=5, fill='x')
frame1.place(relx=0.02,rely=0.05)

left_image = PhotoImage(file='Images/estate.png')
left_image_label = Label(frame1, image=left_image, bg="white")
left_image_label.image = left_image  # Keep a reference to the image
left_image_label.pack(side=LEFT, padx=30)

info_label = Label(frame1, text=f"Insert Name", font=("Arial", 12))
info_label.pack(side=LEFT, padx=10)

view_button = Button(frame1, text="Chat", bg="#B31312", fg='white')
view_button.pack(side=RIGHT, padx=10)

main_window.mainloop()

    # if __name__ == "__main__":
    #     window = Tk()
    #     create_main_window(window)
    #     window.mainloop()