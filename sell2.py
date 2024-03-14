from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkintermapview

class sell2:
    def __init__(self,root):
        self.root = root

        self.add_user_pic = tk.PhotoImage(file='Images/estate.png')

        # def create_self.root(parent):
        #     self.root = Toplevel(parent)

        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 15, "bold")

        one = Label(self.root,
                    text="EstateInsight",
                    bg="#B31312",
                    fg="white",
                    font=font_info,
                    anchor=W,
                    relief=GROOVE,
                    bd=1,
                    height=1)
        one.pack(fill=X, side=TOP)

        # app color
        self.root.configure(bg='mintcream')

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

        # setting up the main parts
        transaction_selection = tk.StringVar()  # gender string def
        possesion_status = tk.StringVar()

        # pic upload
        self.pic_path = tk.StringVar()
        self.pic_path.set('')

        def open_pic():
            path = askopenfilename()

            if path:
                self.img = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                self.pic_path.set(path)

                add_pic_butt.config(image=self.img)
                add_pic_butt.image = self.img

        def open_pic2():
            path = askopenfilename()

            if path:
                self.img2 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                self.pic_path.set(path)

                add_pic2_butt.config(image=self.img2)
                add_pic2_butt.image = self.img2

        self.whole_page_frame = tk.Frame(root, bg='mintcream', highlightthickness=2)

        def open_pic3():
            path = askopenfilename()

            if path:
                self.img3 = ImageTk.PhotoImage(Image.open(path).resize((100, 100)))
                self.pic_path.set(path)

                add_pic3_butt.config(image=self.img3)
                add_pic3_butt.image = self.img3

        self.whole_page_frame = tk.Frame(root, bg='mintcream', highlightthickness=2)

        # --------------------------------------property features-----------------------------------------------#

        # adding top text
        top_text = tk.Label(self.whole_page_frame, text='Property Features',
                            bg='white',
                            fg='black',
                            font=('Microsoft Sans', 15))
        top_text.place(relx=0.01, rely=0.03)

        # No of floors
        enter_floors = tk.Label(self.whole_page_frame, text='Floor No.', font=('Microsoft Sans', 12), bg='white')
        enter_floors.place(relx=0.01, rely=0.1)
        enter_floors_ent = tk.Entry(self.whole_page_frame, font=('Bold', 12),
                                    highlightcolor='black', highlightbackground='gray',
                                    highlightthickness=1)  # name entry button
        enter_floors_ent.place(relx=0.01, rely=0.15)

        # size of flat (bhk)
        bhk = tk.Label(self.whole_page_frame, text='No. of Bedrooms', font=('Microsoft Sans', 12), bg='white')
        bhk.place(relx=0.25, rely=0.1)
        bhk_ent = tk.Entry(self.whole_page_frame, font=('Bold', 12),
                           highlightcolor='black', highlightbackground='gray',
                           highlightthickness=1)
        bhk_ent.place(relx=0.25, rely=0.15)

        # furnished
        furnish = tk.Label(self.whole_page_frame, text='Furnished Status', font=('Microsoft Sans', 12), bg='white')
        furnish.place(relx=0.495, rely=0.1)
        furnish_ent = tk.Entry(self.whole_page_frame, font=('Bold', 12),
                               highlightcolor='black', highlightbackground='gray',
                               highlightthickness=1)
        furnish_ent.place(relx=0.495, rely=0.15)

        # -------------------------------------area text-------------------------------------------------------#

        # area text
        top_text = tk.Label(self.whole_page_frame, text='Area',
                            bg='white',
                            fg='black',
                            font=('Microsoft Sans', 15))
        top_text.place(relx=0.01, rely=0.25)

        # covered area
        covered_area = tk.Label(self.whole_page_frame, text='Covered Area (Sq-ft)', font=('Microsoft Sans', 12), bg='white')
        covered_area.place(relx=0.01, rely=0.32)
        covered_area_ent = tk.Entry(self.whole_page_frame, font=('Bold', 12),
                                    highlightcolor='black', highlightbackground='gray',
                                    highlightthickness=1)  # name entry button
        covered_area_ent.place(relx=0.01, rely=0.37)

        # carpet area
        carpet = tk.Label(self.whole_page_frame, text='Carpet Area(Sq-ft)', font=('Microsoft Sans', 12), bg='white')
        carpet.place(relx=0.25, rely=0.32)
        carpet_ent = tk.Entry(self.whole_page_frame, font=('Bold', 12),
                              highlightcolor='black', highlightbackground='gray',
                              highlightthickness=1)
        carpet_ent.place(relx=0.25, rely=0.37)

        # entrance
        entrance = tk.Label(self.whole_page_frame, text='Width of Entrance (in meters)', font=('Microsoft Sans', 12),
                            bg='white')
        entrance.place(relx=0.495, rely=0.32)
        entrance_ent = tk.Entry(self.whole_page_frame, font=('Bold', 12),
                                highlightcolor='black', highlightbackground='gray',
                                highlightthickness=1)
        entrance_ent.place(relx=0.495, rely=0.37)

        # ------------------------------transaction type----------------------------------------------------------#

        trans_select = tk.Label(self.whole_page_frame, text='Transaction Type:',
                                font=('Bold', 15), bg='white')
        trans_select.place(relx=0.01, rely=0.47)
        new_prop = tk.Radiobutton(self.whole_page_frame, text='New Property',
                                  font=('Bold', 12), bg='white',
                                  variable=transaction_selection, value='new_prop')  # male button
        new_prop.place(relx=0.2, rely=0.47)
        resale = tk.Radiobutton(self.whole_page_frame, text='Resale',
                                font=('Bold', 12), bg='white',
                                variable=transaction_selection, value='resale')  # female button
        resale.place(relx=0.35, rely=0.47)
        transaction_selection.set('new_prop')

        # possesion_status
        possess = tk.Label(self.whole_page_frame, text='Possession Status:',
                           font=('Bold', 15), bg='white')
        possess.place(relx=0.01, rely=0.57)
        cons = tk.Radiobutton(self.whole_page_frame, text='Under Construction',
                              font=('Bold', 12), bg='white',
                              variable=possesion_status, value='cons')  # male button
        cons.place(relx=0.2, rely=0.57)
        ready = tk.Radiobutton(self.whole_page_frame, text='Ready to Move',
                               font=('Bold', 12), bg='white',
                               variable=possesion_status, value='ready')  # female button
        ready.place(relx=0.4, rely=0.57)
        possesion_status.set('cons')

        # -----------------------------adding the profile pic insertion----------------------------------------------------#

        # add images of property text
        top_text = tk.Label(self.whole_page_frame, text='Add Images of Property (upto 4)',
                            bg='white',
                            fg='black',
                            font=('Microsoft Sans', 15))
        top_text.place(relx=0.01, rely=0.7)

        # 1st image
        add_pic_frame = tk.Frame(self.whole_page_frame,
                                 highlightbackground='black',
                                 highlightthickness=2,
                                 bg='white')
        add_pic_butt = tk.Button(add_pic_frame, image=self.add_user_pic, bd=0,
                                 command=open_pic)  # the pic upload button
        add_pic_butt.pack()
        add_pic_frame.place(relx=0.01, rely=0.8, width=105, height=105)

        # 2nd image
        add_pic2_frame = tk.Frame(self.whole_page_frame,
                                  highlightbackground='black',
                                  highlightthickness=2,
                                  bg='white')
        add_pic2_butt = tk.Button(add_pic2_frame, image=self.add_user_pic, bd=0,
                                  command=open_pic2)  # the pic upload button
        add_pic2_butt.pack()
        add_pic2_frame.place(relx=0.2, rely=0.8, width=105, height=105)

        # 3rd image
        add_pic3_frame = tk.Frame(self.whole_page_frame,
                                  highlightbackground='black',
                                  highlightthickness=2,
                                  bg='white')
        add_pic3_butt = tk.Button(add_pic3_frame, image=self.add_user_pic, bd=0,
                                  command=open_pic3)  # the pic upload button
        add_pic3_butt.pack()
        add_pic3_frame.place(relx=0.4, rely=0.8, width=105, height=105)

        # ----------------------------------------save button-------------------------------------------------#

        submit_butt = tk.Button(self.whole_page_frame, text="Save",
                                font=('Bold', 15), bg='#B31312',
                                fg='white', bd=1)
        submit_butt.place(relx=0.7, rely=0.85)

        self.whole_page_frame.pack(pady=3)
        self.whole_page_frame.pack_propagate(False)
        self.whole_page_frame.configure(width=980, height=600)

root=Tk()
obj = sell2(root)
root.mainloop()
