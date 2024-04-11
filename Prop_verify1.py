from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk

from tkinter import messagebox
from mysql.connector import Error
import mysql.connector


class prop_verify1:
    def __init__(self,root):
        self.root = root
        self.add_user_pic = tk.PhotoImage(file='Images/estate.png')

        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

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
        self.root.configure(bg='white')

        # setting up geometry for app
        window_width = 1000
        window_height = 660

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # setting up icon for window title
        self.icon = PhotoImage(file='Images/estate.png')
        root.iconphoto(True, self.icon)
#***************************** connecting to database **********************************
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='ARYA#305#varun',
                database='estateinsight'
            )
            print("Connected to MySQL")
        except Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Database Error", "Failed to connect to database")
            return

# ********************************setting up the main page***************************#

        # setting the strings of radio buttons
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
                self.img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                pic_path.set(path)

                add_pic_butt.config(image=self.img)
                add_pic_butt.image = self.img

        def open_pic2():
            path = askopenfilename()

            if path:
                self.img2 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                pic_path.set(path)

                add_pic2_butt.config(image=self.img2)
                add_pic2_butt.image = self.img2

        def open_pic3():
            path = askopenfilename()

            if path:
                self.img3 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                pic_path.set(path)

                add_pic3_butt.config(image=self.img3)
                add_pic3_butt.image = self.img3


        def open_pic4():
            path = askopenfilename()

            if path:
                self.img4 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                pic_path.set(path)

                add_pic4_butt.config(image=self.img4)
                add_pic4_butt.image = self.img4

        # adding top text
        top_text = tk.Label(root, text='Property Details',
                            bg='white',
                            fg='black',
                            font=('Bold', 20))
        top_text.place(relx=0.01, rely=0.06)

        # *********************************************************************************************************************

        enter_name = tk.Label(root, text='>Property Name:', font=('Bold', 15), bg='white')
        enter_name.place(relx=0.01, rely=0.15)
        enter_name_ent = tk.Label(root, font=('Bold', 15),
                                  highlightcolor='black', highlightbackground='gray',
                                  highlightthickness=2)  # name entry button
        enter_name_ent.place(relx=0.01, rely=0.2)

        # *********************************************************************************************************************

        register_select = tk.Label(root, text='Registered as:',
                                   font=('Bold', 15), bg='white')
        register_select.place(relx=0.01, rely=0.3)
        register_select_lab = tk.Label(root, font=('Bold', 15),
                                       highlightcolor='black', highlightbackground='gray',
                                       highlightthickness=2)
        register_select_lab.place(relx=0.01, rely=0.35)

        # *********************************************************************************************************************

        transaction_select = tk.Label(root, text='Transaction Type:',
                                      font=('Bold', 15), bg='white')
        transaction_select.place(relx=0.5, rely=0.3)
        transaction_select_lab = tk.Label(root, font=('Bold', 15),
                                          highlightcolor='black', highlightbackground='gray',
                                          highlightthickness=2)
        transaction_select_lab.place(relx=0.5, rely=0.35)

        # *******************************************************************************************************************

        status_select = tk.Label(root, text='Address:',
                                 font=('Bold', 15), bg='white')
        status_select.place(relx=0.01, rely=0.45)
        status_select_lab = tk.Label(root, font=('Bold', 15),
                                     highlightcolor='black', highlightbackground='gray',
                                     highlightthickness=2)
        status_select_lab.place(relx=0.01, rely=0.5)

        # *********************************************************************************************************************


        ownership_select = tk.Label(root, text='>Landmark:',
                                    font=('Bold', 15), bg='white')
        ownership_select.place(relx=0.5, rely=0.45)
        ownership_select_lab = tk.Label(root, font=('Bold', 15),
                                        highlightcolor='black', highlightbackground='gray',
                                        highlightthickness=2)
        ownership_select_lab.place(relx=0.5, rely=0.5)

        # pic add

        # add images of property text
        top_text = tk.Label(root, text='Images of Property:',
                            bg='white',
                            fg='black',
                            font=('Bold', 15))
        top_text.place(relx=0.01, rely=0.63)

        top_text2 = tk.Label(root, text='ID Proof:',
                            bg='white',
                            fg='black',
                            font=('Bold', 15))
        top_text2.place(relx=0.63, rely=0.63)

        # 1st image
        add_pic_frame = tk.Frame(root,
                                 highlightbackground='black',
                                 highlightthickness=2,
                                 bg='white')
        add_pic_butt = tk.Button(add_pic_frame, image=self.add_user_pic, bd=0,
                                 command=open_pic)  # the pic upload button
        add_pic_butt.pack()
        add_pic_frame.place(relx=0.01, rely=0.73, width=105, height=105)

        # 2nd image
        add_pic2_frame = tk.Frame(root,
                                  highlightbackground='black',
                                  highlightthickness=2,
                                  bg='white')
        add_pic2_butt = tk.Button(add_pic2_frame, image=self.add_user_pic, bd=0,
                                  command=open_pic2)  # the pic upload button
        add_pic2_butt.pack()
        add_pic2_frame.place(relx=0.16, rely=0.73, width=105, height=105)

        # 3rd image
        add_pic3_frame = tk.Frame(root,
                                  highlightbackground='black',
                                  highlightthickness=2,
                                  bg='white')
        add_pic3_butt = tk.Button(add_pic3_frame, image=self.add_user_pic, bd=0,
                                  command=open_pic3)  # the pic upload button
        add_pic3_butt.pack()
        add_pic3_frame.place(relx=0.32, rely=0.73, width=105, height=105)

        # 4th image
        add_pic4_frame = tk.Frame(root,
                                  highlightbackground='black',
                                  highlightthickness=2,
                                  bg='white')
        add_pic4_butt = tk.Button(add_pic4_frame, image=self.add_user_pic, bd=0,
                                  command=open_pic4)  # the pic upload button
        add_pic4_butt.pack()
        add_pic4_frame.place(relx=0.62, rely=0.73, width=105, height=105)

        # adding the next button
        verify = tk.Button(root, text="Verify",
                              font=('Bold', 15), bg='#B31312',
                              fg='white', bd=1)
        verify.place(relx=0.85, rely=0.7)

        notverify = tk.Button(root, text="Not Verify",
                              font=('Bold', 15), bg='#B31312',
                              fg='white', bd=1)
        notverify.place(relx=0.85, rely=0.8)



root=Tk()
obj = prop_verify1(root)
root.mainloop()