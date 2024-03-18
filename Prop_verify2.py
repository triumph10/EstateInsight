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

#****************************setting the main part*****************************************

# adding top text
top_text = tk.Label(root, text='More Property Details',
                            bg='white',
                            fg='black',
                            font=('Bold', 20))
top_text.place(relx=0.01, rely=0.06)

#Area part

area_text = tk.Label(root, text='Area Details:',
                     bg='white',
                     fg='black',
                     font=('Microsoft Sans',17))
area_text.place(relx=0.01, rely=0.15)

#******************************************************************************************************************

#carpet area
# carpet_area = tk.Label(root, text='>Carpet Area', font=('Bold', 15), bg='white')
# carpet_area.place(relx=0.01, rely=0.21)
# carpet_area_ent = tk.Entry(root, font=('Bold', 15),
#                           highlightcolor='black', highlightbackground='gray',
#                           highlightthickness=2)
# carpet_area_ent.place(relx=0.01, rely=0.26)
carpet_area = tk.Label(root, text='>Carpet Area', font=('Bold', 15), bg='white')
carpet_area.place(relx=0.01, rely=0.21)
carpet_area_lab = tk.Label(root, font=('Bold', 15),
                          highlightcolor='black', highlightbackground='gray',
                          highlightthickness=2)
carpet_area_lab.place(relx=0.01, rely=0.26)

#*******************************************************************************************************************

#carpet area/sq.ft
# carpet_price = tk.Label(root, text='>Price/Sq.Ft', font=('Bold', 15), bg='white')
# carpet_price.place(relx=0.26, rely=0.21)
# carpet_price_ent = tk.Entry(root, font=('Bold', 15),
#                             highlightcolor='black', highlightbackground='gray',
#                             highlightthickness=2)
# carpet_price_ent.place(relx=0.26, rely=0.26)
carpet_price = tk.Label(root, text='>Price/Sq.Ft', font=('Bold', 15), bg='white')
carpet_price.place(relx=0.26, rely=0.21)
carpet_price_lab = tk.Label(root, font=('Bold', 15),
                            highlightcolor='black', highlightbackground='gray',
                            highlightthickness=2)
carpet_price_lab.place(relx=0.26, rely=0.26)

#*********************************************************************************************************************

#floors
# floor = tk.Label(root, text='>Floor', font=('Bold', 15), bg='white')
# floor.place(relx=0.51, rely=0.21)
# floor_ent = tk.Entry(root, font=('Bold', 15),
#                      highlightcolor='black', highlightbackground='gray',
#                      highlightthickness=2)
# floor_ent.place(relx=0.51, rely=0.26)
floor = tk.Label(root, text='>Floor', font=('Bold', 15), bg='white')
floor.place(relx=0.51, rely=0.21)
floor_lab = tk.Label(root, font=('Bold', 15),
                     highlightcolor='black', highlightbackground='gray',
                     highlightthickness=2)
floor_lab.place(relx=0.51, rely=0.26)

#********************************************************************************************************************

#out of floors
# floor_out = tk.Label(root, text='>Number of Floors', font=('Bold', 15), bg='white')
# floor_out.place(relx=0.76, rely=0.21)
# floor_out_ent = tk.Entry(root, font=('Bold', 15),
#                      highlightcolor='black', highlightbackground='gray',
#                      highlightthickness=2)
# floor_out_ent.place(relx=0.76, rely=0.26)
floor_out = tk.Label(root, text='>Number of Floors', font=('Bold', 15), bg='white')
floor_out.place(relx=0.76, rely=0.21)
floor_out_lab = tk.Label(root, font=('Bold', 15),
                     highlightcolor='black', highlightbackground='gray',
                     highlightthickness=2)
floor_out_lab.place(relx=0.76, rely=0.26)

#*******************************************************************************************************************

#location part

location_text = tk.Label(root, text='Location Details:',
                     bg='white',
                     fg='black',
                     font=('Microsoft Sans',17))
location_text.place(relx=0.01, rely=0.36)

#*******************************************************************************************************************

#adress
# address = tk.Label(root, text='>Address', font=('Bold', 15), bg='white')
# address.place(relx=0.01, rely=0.42)
# address_ent = tk.Entry(root, font=('Bold', 15),
#                        highlightcolor='black', highlightbackground='gray',
#                        highlightthickness=2)
# address_ent.place(relx=0.01, rely=0.47)
address = tk.Label(root, text='>Address', font=('Bold', 15), bg='white')
address.place(relx=0.01, rely=0.42)
address_lab = tk.Label(root, font=('Bold', 15),
                       highlightcolor='black', highlightbackground='gray',
                       highlightthickness=2)
address_lab.place(relx=0.01, rely=0.47)

#**********************************************************************************************************************

#landmarks
# landmark = tk.Label(root, text='>Landmark', font=('Bold', 15), bg='white')
# landmark.place(relx=0.3, rely=0.42)
# landmark_ent = tk.Entry(root, font=('Bold', 15),
#                         highlightcolor='black', highlightbackground='gray',
#                         highlightthickness=2)
# landmark_ent.place(relx=0.3, rely=0.47)
landmark = tk.Label(root, text='>Landmark', font=('Bold', 15), bg='white')
landmark.place(relx=0.3, rely=0.42)
landmark_lab = tk.Label(root, font=('Bold', 15),
                        highlightcolor='black', highlightbackground='gray',
                        highlightthickness=2)
landmark_lab.place(relx=0.3, rely=0.47)

#*******************************************************************************************************************

#pricing part

pricing_text = tk.Label(root, text='Pricing Details:',
                        bg='white',
                        fg='black',
                        font=('Microsoft Sans',17))
pricing_text.place(relx=0.01, rely=0.57)

#price
# price = tk.Label(root, text='>Price', font=('Bold', 15), bg='white')
# price.place(relx=0.01, rely=0.63)
# price_ent = tk.Entry(root, font=('Bold', 15),
#                      highlightcolor='black', highlightbackground='gray',
#                      highlightthickness=2)
# price_ent.place(relx=0.01, rely=0.68)
price = tk.Label(root, text='>Price', font=('Bold', 15), bg='white')
price.place(relx=0.01, rely=0.63)
price_lab = tk.Label(root, font=('Bold', 15),
                     highlightcolor='black', highlightbackground='gray',
                     highlightthickness=2)
price_lab.place(relx=0.01, rely=0.68)

#*********************************************************************************************************************

#booking
# booking = tk.Label(root, text='>Booking', font=('Bold', 15), bg='white')
# booking.place(relx=0.3, rely=0.63)
# booking_ent = tk.Entry(root, font=('Bold', 15),
#                        highlightcolor='black', highlightbackground='gray',
#                        highlightthickness=2)
# booking_ent.place(relx=0.3, rely=0.68)
booking = tk.Label(root, text='>Booking', font=('Bold', 15), bg='white')
booking.place(relx=0.3, rely=0.63)
booking_lab = tk.Label(root, font=('Bold', 15),
                       highlightcolor='black', highlightbackground='gray',
                       highlightthickness=2)
booking_lab.place(relx=0.3, rely=0.68)

#next button
next_butt = tk.Button(root, text="Next",
                      font=('Bold', 15), bg='#B31312',
                      fg='white', bd=1)
next_butt.place(relx=0.5, rely=0.87, anchor=CENTER)















root.mainloop()