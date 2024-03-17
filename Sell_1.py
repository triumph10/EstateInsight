from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk



root = tk.Tk()

add_user_pic = tk.PhotoImage(file='Images/estate.png')

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

#********************************setting up the main page***************************

#setting the strings of radio buttons
registered_selection = tk.StringVar()
transaction_selection = tk.StringVar()
status_selection = tk.StringVar()
ownership_selection = tk.StringVar()

# pic upload
pic_path = tk.StringVar()
pic_path.set('')

def open_pic():
    path = askopenfilename()

    if path:
        img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
        pic_path.set(path)

        add_pic_butt.config(image=img)
        add_pic_butt.image = img

def open_pic2():
    path = askopenfilename()

    if path:
       img2 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
       pic_path.set(path)

       add_pic2_butt.config(image=img2)
       add_pic2_butt.image = img2



def open_pic3():
    path = askopenfilename()

    if path:
       img3 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
       pic_path.set(path)

       add_pic3_butt.config(image=img3)
       add_pic3_butt.image = img3




# adding top text
top_text = tk.Label(root, text='Property Details',
                            bg='white',
                            fg='black',
                            font=('Bold', 20))
top_text.place(relx=0.01, rely=0.06)

# adding name entry box
enter_name = tk.Label(root, text='>Property Name:', font=('Bold', 15), bg='white')
enter_name.place(relx=0.01, rely=0.15)
enter_name_ent = tk.Entry(root, font=('Bold', 15),
                          highlightcolor='black', highlightbackground='gray',
                          highlightthickness=2)  # name entry button
enter_name_ent.place(relx=0.01, rely=0.2)

# adding register selection
register_select = tk.Label(root, text='>Register as:',
                           font=('Bold', 15), bg='white')
register_select.place(relx=0.01, rely=0.3)
owner = tk.Radiobutton(root, text='Male',
                      font=('Bold', 15), bg='white',
                      variable=registered_selection, value='owner')
owner.place(relx=0.01, rely=0.35)
builder = tk.Radiobutton(root, text='Builder',
                        font=('Bold', 15), bg='white',
                        variable=registered_selection, value='builder')
builder.place(relx=0.1, rely=0.35)
registered_selection.set('owner')

# adding transaction selection
transaction_select = tk.Label(root, text='>Transaction Type:',
                              font=('Bold', 15), bg='white')
transaction_select.place(relx=0.5, rely=0.3)
new_property = tk.Radiobutton(root, text='New Property',
                             font=('Bold', 15), bg='white',
                             variable=transaction_selection, value='new_property')
new_property.place(relx=0.5, rely=0.35)
resale = tk.Radiobutton(root, text='Resale',
                        font=('Bold', 15), bg='white',
                        variable=transaction_selection, value='resale')
resale.place(relx=0.66, rely=0.35)
transaction_selection.set('new_property')

# adding status selection
status_select = tk.Label(root, text='>Status:',
                           font=('Bold', 15), bg='white')
status_select.place(relx=0.01, rely=0.45)
Un_construct = tk.Radiobutton(root, text='Under Construction',
                              font=('Bold', 15), bg='white',
                              variable=status_selection, value='Un_construct')
Un_construct.place(relx=0.01, rely=0.5)
ready = tk.Radiobutton(root, text='Ready to Move',
                       font=('Bold', 15), bg='white',
                       variable=status_selection, value='ready')
ready.place(relx=0.22, rely=0.5)
status_selection.set('Un_construct')

# adding ownership selection
ownership_select = tk.Label(root, text='>Type of Ownership:',
                            font=('Bold', 15), bg='white')
ownership_select.place(relx=0.5, rely=0.45)
house = tk.Radiobutton(root, text='House',
                       font=('Bold', 15), bg='white',
                       variable=ownership_selection, value='house')
house.place(relx=0.5, rely=0.5)
villa = tk.Radiobutton(root, text='Villa',
                       font=('Bold', 15), bg='white',
                       variable=ownership_selection, value='villa')
villa.place(relx=0.6, rely=0.5)
society = tk.Radiobutton(root, text='Co-Operative Society',
                         font=('Bold', 15), bg='white',
                         variable=ownership_selection, value='society')
society.place(relx=0.69, rely=0.5)
ownership_selection.set('house')

#pic add

# add images of property text
top_text = tk.Label(root, text='Add Images of Property:',
                          bg='white',
                          fg='black',
                          font=('Bold', 17))
top_text.place(relx=0.01, rely=0.63)

# 1st image
add_pic_frame = tk.Frame(root,
                         highlightbackground='black',
                         highlightthickness=2,
                         bg='white')
add_pic_butt = tk.Button(add_pic_frame, image=add_user_pic, bd=0,
                         command=open_pic)  # the pic upload button
add_pic_butt.pack()
add_pic_frame.place(relx=0.01, rely=0.73, width=105, height=105)

# 2nd image
add_pic2_frame = tk.Frame(root,
                          highlightbackground='black',
                          highlightthickness=2,
                          bg='white')
add_pic2_butt = tk.Button(add_pic2_frame, image=add_user_pic, bd=0,
                          command=open_pic2)  # the pic upload button
add_pic2_butt.pack()
add_pic2_frame.place(relx=0.16, rely=0.73, width=105, height=105)

# 3rd image
add_pic3_frame = tk.Frame(root,
                          highlightbackground='black',
                          highlightthickness=2,
                          bg='white')
add_pic3_butt = tk.Button(add_pic3_frame, image=add_user_pic, bd=0,
                          command=open_pic3)  # the pic upload button
add_pic3_butt.pack()
add_pic3_frame.place(relx=0.32, rely=0.73, width=105, height=105)

# adding the next button
next_butt = tk.Button(root, text="Next",
                      font=('Bold', 15), bg='#B31312',
                      fg='white', bd=1)
next_butt.place(relx=0.6, rely=0.8)

# setting up the back page button

back_button = Button(root, bg='#B31312', fg='white', text='<<Back')
back_button.place(relx=0.9, rely=0.1)

root.mainloop()