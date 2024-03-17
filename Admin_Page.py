from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()

img_butt_add1 = PhotoImage(file='Images/prop_verify.png')
img_butt_add2 = PhotoImage(file='Images/prop_upload.png')
img_butt_add3 = PhotoImage(file='Images/price_graph.png')


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
name_label.place(relx=0.85,rely=0.1) #name
down_arrow = Menubutton(one, text='˅' ,bd=0, bg='#B31312', fg='white')
down_arrow.pack()
down_arrow.menu = Menu(down_arrow)
down_arrow["menu"] = down_arrow.menu
down_arrow.menu.add_checkbutton(label="Profile")
down_arrow.menu.add_checkbutton(label="Agents")
down_arrow.place(relx=0.92)#drop down arrow

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

#*******************************Top Heading************************************************

heading_label = Label(root, text="Admin Page", font=('Microsoft Yahei UI Light',25), bd=0, bg='white')
heading_label.place(relx=0.41, rely=0.1)

#*******************************adding the main widgets*************************************

#1st frame
whole_fm1 = Frame(root,
                  highlightthickness=2,
                  width=315,
                  height=400,
                  bg='white',
                  highlightbackground='black')

frame1 = Frame(whole_fm1,
               background='white',
               highlightbackground='black',
               bd=0)
img_butt = Button(frame1,
                  image=img_butt_add1,
                  bd=0,
                  width=120,
                  height=120)
img_butt.pack()
frame1.place(relx=0.3, rely=0.3)

name_button = Button(whole_fm1,
                     text='Property\nVerification',
                     font=('Bold',17),
                     bg='white',bd=0)
name_button.place(relx=0.30, rely=0.7)
whole_fm1.place(relx=0.01, rely=0.25)

#2nd frame
whole_fm2 = Frame(root,
                  highlightthickness=2,
                  width=315,
                  height=400,
                  bg='white',
                  highlightbackground='black')

frame2 = Frame(whole_fm2,
               background='white',
               highlightbackground='black',
               bd=0)
img_butt = Button(frame2,
                  image=img_butt_add2,
                  bd=0,
                  width=120,
                  height=120)
img_butt.pack()
frame2.place(relx=0.3, rely=0.3)

name_button = Button(whole_fm2,
                     text='Property\nUpload',
                     font=('Bold',17),
                     bg='white',bd=0)
name_button.place(relx=0.30, rely=0.7)
whole_fm2.place(relx=0.34, rely=0.25)

#3rd frame
whole_fm3 = Frame(root,
                  highlightthickness=2,
                  width=315,
                  height=400,
                  bg='white',
                  highlightbackground='black')

frame3 = Frame(whole_fm3,
               background='white',
               highlightbackground='black',
               bd=0)
img_butt = Button(frame3,
                  image=img_butt_add3,
                  bd=0,
                  width=120,
                  height=120)
img_butt.pack()
frame3.place(relx=0.3, rely=0.3)

name_button = Button(whole_fm3,
                     text='Land Value\nGraph',
                     font=('Bold',17),
                     bg='white',bd=0)
name_button.place(relx=0.30, rely=0.7)
whole_fm3.place(relx=0.67, rely=0.25)

root.mainloop()