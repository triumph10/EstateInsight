from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

root = Tk()

# setting up the app
root.title("EstateInsight")
root.resizable(False, False)

font_info = ("Arial", 15, "bold")

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
                   text='Insert Name',
                   bg='#B31312',
                   fg='white',
                   bd=0)
name_label.place(relx=0.85, rely=0.1)  # name
down_arrow = Menubutton(one, text='˅', bd=0, bg='#B31312', fg='white')
down_arrow.pack()
down_arrow.menu = Menu(down_arrow)
down_arrow["menu"] = down_arrow.menu
down_arrow.menu.add_checkbutton(label="Profile")
down_arrow.menu.add_checkbutton(label="Agents")
down_arrow.place(relx=0.92)  # drop down arrow

# app color
root.configure(bg='white')

# setting up geometry for app
window_width = 1000
window_height = 660

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# setting up icon for window title
icon = PhotoImage(file='Images/estate.png')
root.iconphoto(True, icon)

#****************************setting the main part*******************************

#top text
top_text = tk.Label(root, text='Additional Property Details',
                    bg='white',
                    fg='black',
                    font=('Bold', 20))
top_text.place(relx=0.01, rely=0.08)

#furnishing status
furnishing = tk.Label(root, text='>Furnishing Status:', font=('Bold', 17), bg='white')
furnishing.place(relx=0.01, rely=0.21)
furnishing_ent = tk.Entry(root, font=('Bold', 17),
                          highlightcolor='black', highlightbackground='gray',
                          highlightthickness=2)
furnishing_ent.place(relx=0.01, rely=0.26)

#Flooring
flooring = tk.Label(root, text='>Flooring:', font=('Bold', 17), bg='white')
flooring.place(relx=0.5, rely=0.21)
flooring_ent = tk.Entry(root, font=('Bold', 17),
                        highlightcolor='black', highlightbackground='gray',
                        highlightthickness=2)
flooring_ent.place(relx=0.5, rely=0.26)

#overlooking
overlooking = tk.Label(root, text='>Overlooking:', font=('Bold', 17), bg='white')
overlooking.place(relx=0.01, rely=0.41)
overlooking_ent = tk.Entry(root, font=('Bold', 17),
                          highlightcolor='black', highlightbackground='gray',
                          highlightthickness=2)
overlooking_ent.place(relx=0.01, rely=0.46)

#age of construction
construction = tk.Label(root, text='>Age of Construction:', font=('Bold', 17), bg='white')
construction.place(relx=0.5, rely=0.41)
furnishing_ent = tk.Entry(root, font=('Bold', 17),
                          highlightcolor='black', highlightbackground='gray',
                          highlightthickness=2)
furnishing_ent.place(relx=0.5, rely=0.46)

#water availaibility
water = tk.Label(root, text='>Water Availability:', font=('Bold', 17), bg='white')
water.place(relx=0.01, rely=0.61)
water_ent = tk.Entry(root, font=('Bold', 17),
                     highlightcolor='black', highlightbackground='gray',
                     highlightthickness=2)
water_ent.place(relx=0.01, rely=0.66)

#electricity status
electric = tk.Label(root, text='>Electricity Status:', font=('Bold', 17), bg='white')
electric.place(relx=0.5, rely=0.61)
electric_ent = tk.Entry(root, font=('Bold', 17),
                        highlightcolor='black', highlightbackground='gray',
                        highlightthickness=2)
electric_ent.place(relx=0.5, rely=0.66)

# adding the submit button
submit_butt = tk.Button(root, text="Submit",
                        font=('Bold', 15), bg='#B31312',
                        fg='white', bd=1)
submit_butt.place(relx=0.5, rely=0.85, anchor=CENTER)


root.mainloop()