from tkinter import *
from tkinter import ttk


main_window = Tk()

img_butt_add = PhotoImage(file='Images/profile.png')




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
main_window.configure(bg='white')



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

#1st frame
whole_fm1 = Frame(main_window, highlightthickness=2, width=450, height=200, bg='white', highlightbackground='black')

frame1 = Frame(whole_fm1, background='white',highlightbackground='black',
                         highlightthickness=2)
img_butt = Button(frame1, image=img_butt_add, bd=1, width=120, height=120)
img_butt.pack()
frame1.place(relx=0.03, rely=0.06)

chat_button = Button(whole_fm1, text="Chat", bg='#B31312', fg='white')
chat_button.place(relx=0.12, rely=0.76)

name_label = Label(whole_fm1, text='Insert Name', font=('Bold',17), bg='white')
name_label.place(relx=0.35, rely=0.09)

email_label = Label(whole_fm1, text='Email:', font=('Bold',15), bg='white')
email_label.place(relx=0.35, rely=0.3)
ename_label = Label(whole_fm1, text='Insert Email', font=(15), bg='white')
ename_label.place(relx=0.49, rely=0.3)

phone_label = Label(whole_fm1, text='Phone No:', font=('Bold',15), bg='white')
phone_label.place(relx=0.35,rely=0.49)
number_label = Label(whole_fm1, text='Insert No.', font=(15), bg='white')
number_label.place(relx=0.58, rely=0.49)

whole_fm1.place(relx=0.02, rely=0.15)

#2nd frame
whole_fm2 = Frame(main_window, highlightthickness=2, width=450, height=200, bg='white', highlightbackground='black')

frame2 = Frame(whole_fm2, background='white',highlightbackground='black',
                         highlightthickness=2)
img_butt = Button(frame2, image=img_butt_add, bd=1, width=120, height=120)
img_butt.pack()
frame2.place(relx=0.03, rely=0.06)

chat_button = Button(whole_fm2, text="Chat", bg='#B31312', fg='white')
chat_button.place(relx=0.12, rely=0.76)

name_label = Label(whole_fm2, text='Insert Name', font=('Bold',17), bg='white')
name_label.place(relx=0.35, rely=0.09)

email_label = Label(whole_fm2, text='Email:', font=('Bold',15), bg='white')
email_label.place(relx=0.35, rely=0.3)
ename_label = Label(whole_fm2, text='Insert Email', font=(15), bg='white')
ename_label.place(relx=0.49, rely=0.3)

phone_label = Label(whole_fm2, text='Phone No:', font=('Bold',15), bg='white')
phone_label.place(relx=0.35,rely=0.49)
number_label = Label(whole_fm2, text='Insert No.', font=(15), bg='white')
number_label.place(relx=0.58, rely=0.49)

whole_fm2.place(relx=0.5, rely=0.15)

#3rd frame
whole_fm3 = Frame(main_window, highlightthickness=2, width=450, height=200, bg='white', highlightbackground='black')

frame3 = Frame(whole_fm3, background='white',highlightbackground='black',
                         highlightthickness=2)
img_butt = Button(frame3, image=img_butt_add, bd=1, width=120, height=120)
img_butt.pack()
frame3.place(relx=0.03, rely=0.06)

chat_button = Button(whole_fm3, text="Chat", bg='#B31312', fg='white')
chat_button.place(relx=0.12, rely=0.76)

name_label = Label(whole_fm3, text='Insert Name', font=('Bold',17), bg='white')
name_label.place(relx=0.35, rely=0.09)

email_label = Label(whole_fm3, text='Email:', font=('Bold',15), bg='white')
email_label.place(relx=0.35, rely=0.3)
ename_label = Label(whole_fm3, text='Insert Email', font=(15), bg='white')
ename_label.place(relx=0.49, rely=0.3)

phone_label = Label(whole_fm3, text='Phone No:', font=('Bold',15), bg='white')
phone_label.place(relx=0.35,rely=0.49)
number_label = Label(whole_fm3, text='Insert No.', font=(15), bg='white')
number_label.place(relx=0.58, rely=0.49)

whole_fm3.place(relx=0.02, rely=0.55)

#4th frame
whole_fm4 = Frame(main_window, highlightthickness=2, width=450, height=200, bg='white', highlightbackground='black')

frame4 = Frame(whole_fm4, background='white',highlightbackground='black',
                         highlightthickness=2)
img_butt = Button(frame4, image=img_butt_add, bd=1, width=120, height=120)
img_butt.pack()
frame4.place(relx=0.03, rely=0.06)

chat_button = Button(whole_fm4, text="Chat", bg='#B31312', fg='white')
chat_button.place(relx=0.12, rely=0.76)

name_label = Label(whole_fm4, text='Insert Name', font=('Bold',17), bg='white')
name_label.place(relx=0.35, rely=0.09)

email_label = Label(whole_fm4, text='Email:', font=('Bold',15), bg='white')
email_label.place(relx=0.35, rely=0.3)
ename_label = Label(whole_fm4, text='Insert Email', font=(15), bg='white')
ename_label.place(relx=0.49, rely=0.3)

phone_label = Label(whole_fm4, text='Phone No:', font=('Bold',15), bg='white')
phone_label.place(relx=0.35,rely=0.49)
number_label = Label(whole_fm4, text='Insert No.', font=(15), bg='white')
number_label.place(relx=0.58, rely=0.49)

whole_fm4.place(relx=0.5, rely=0.55)

# setting up the back page button

back_button = Button(main_window, bg='#B31312', fg='white', text='<<Back')
back_button.place(relx=0.88, rely=0.08)



main_window.mainloop()

