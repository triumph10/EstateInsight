from tkinter import *
from tkinter import ttk


class sell1:
    def __init__(self,root):
        self.root = root

        # setting up the app
        self.root.title("EstateInsight")
        self.root.resizable(False, False)

        font_info = ("Arial", 15, "bold")

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
        self.root.iconphoto(True, self.icon)

        one = Label(root,
                    text="EstateInsight",
                    bg="RED",
                    fg="WHITE",
                    font=font_info,
                    anchor=W,
                    relief=SUNKEN,
                    bd=1,
                    pady=3)
        one.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        radio_label = Label(root, text="Select Role:", font=("Arial", 12), bg="mintcream")
        radio_label.grid(row=2, column=0, columnspan=3, pady=(20, 5))

        loginbutton = Button(root, text="Login", bg="RED", border=0, activebackground='#B67352', fg='WHITE')
        loginbutton.grid(row=0, column=0, columnspan=3, padx=(10, 200), pady=12, sticky='ne')

        signupbutton = Button(root, text="Signup", bg="RED", border=0, activebackground='PINK', fg='WHITE')
        signupbutton.grid(row=0, column=0, columnspan=3, padx=(10, 100), pady=12, sticky='ne')

        toolbar = Frame(root, bg="#38419D", relief=SUNKEN, bd=1, pady=2, height=4)
        toolbar.grid(row=1, column=0, columnspan=3, padx=500, pady=10, sticky='ew')

        seller = ["Owner", "Agent", "Builder"]

        def owner_function():
            frame1 = Frame(root,
                           width=600,
                           height=1000,
                           bg="mintcream",
                           relief=GROOVE)

            def on_enter(e):  # Clear the content of the entry field
                confirm_pass.delete(0, 'end')

            def on_leave(e):  # Check if the entry field is empty
                if confirm_pass.get() == '':
                    confirm_pass.insert(0, 'Enter Your Name')  # if the field is empty insert the text

            confirm_pass = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                                 font=('Microsoft Yahel UI Light', 11))
            confirm_pass.place(x=350, y=220)
            confirm_pass.insert(0, 'Enter Your Name')
            confirm_pass.bind("<FocusIn>", on_enter)  # user clicks on the field, the on enter fucntion is called
            confirm_pass.bind("<FocusOut>", on_leave)  # is the field is empty on leave function is called

            Frame(root, width=295, height=2, bg="black").grid(row=10, column=0, padx=350, pady=80)

            ###############################

            def on_enter2(e):
                phono.delete(0, 'end')

            def on_leave2(e):
                if phono.get() == '':
                    phono.insert(0, 'Enter Phone Number')

            phono = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                          font=('Microsoft Yahel UI Light', 11))
            phono.place(x=350, y=280)
            phono.insert(0, 'Enter Phone Number')
            phono.bind("<FocusIn>", on_enter2)
            phono.bind("<FocusOut>", on_leave2)

            Frame(root, width=295, height=2, bg="black").place(x=350, y=310)
            ####--------------------------------------------------------------------------------

            vend = ["Sell", "Rent"]

            label1 = Label(root, padx=100, text="Property Details", font=("Microsoft Sans", 14), bg="mintcream")
            label1.grid(row=16, column=0, columnspan=5, sticky="n")  # property details LABEL

            label2 = Label(root, padx=100, text="Property Location", font=("Microsoft Sans", 14), bg="mintcream")
            label2.grid(row=18, column=0, columnspan=5, sticky="n")  # location LABEL

            # -----------------------------------------------------------------------------------
            def on_enter3(e):  # enter city
                city.delete(0, 'end')

            def on_leave3(e):
                if city.get() == '':
                    city.insert(0, 'Enter City')

            city = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                         font=('Microsoft Yahel UI Light', 11))
            city.place(x=350, y=480)
            city.insert(0, 'Enter City')
            city.bind("<FocusIn>", on_enter3)
            city.bind("<FocusOut>", on_leave3)

            Frame(root, width=295, height=2, bg="black").place(x=350, y=510)

            # ----------------------------------------------------------------------------------------

            def on_enter4(e):  # enter locality
                localty.delete(0, 'end')

            def on_leave4(e):
                if localty.get() == '':
                    localty.insert(0, 'Enter Locality')

            localty = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                            font=('Microsoft Yahel UI Light', 11))
            localty.place(x=350, y=540)
            localty.insert(0, 'Enter Locality')
            localty.bind("<FocusIn>", on_enter4)
            localty.bind("<FocusOut>", on_leave4)

            Frame(root, width=295, height=2, bg="black").place(x=350, y=570)
            # ------------------------------------------------------------------------------------------

            radio_frame = Frame(root, bg="mintcream")
            radio_frame.grid(row=17, column=0, columnspan=5, sticky="n")

            # Use grid to arrange radio buttons horizontally
            x = IntVar()
            for index in range(len(vend)):
                radiobutton = Radiobutton(
                    radio_frame,
                    text=vend[index],
                    variable=x,
                    value=index,
                    padx=10,
                    font=("Microsoft Sans", 12))
                radiobutton.grid(row=3, column=index, padx=15, pady=30)
            submit_butt = Button(root, text="Save",
                                 font=('Bold', 15), bg='#B31312',
                                 fg='white', bd=1)
            submit_butt.place(relx=0.458, rely=0.9)
            frame1.place(relx=0.1, rely=0.25)

        # ----------------------------------------------------------------------------------------------------
        def agent_function():
            frame1 = Frame(root,
                           width=600,
                           height=1000,
                           bg="mintcream",
                           relief=GROOVE)

            def on_enter5(e):
                enter_id.delete(0, 'end')

            def on_leave5(e):
                if enter_id.get() == '':
                    enter_id.insert(0, 'Enter Your ID')

            enter_id = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                             font=('Microsoft Yahel UI Light', 11))
            enter_id.place(x=350, y=220)
            enter_id.insert(0, 'Enter Your ID')
            enter_id.bind("<FocusIn>", on_enter5)
            enter_id.bind("<FocusOut>", on_leave5)

            Frame(root, width=295, height=2, bg="black").grid(row=10, column=0, padx=350, pady=80)

            vend2 = ["Sell", "Rent"]
            label1 = Label(root, padx=100, text="Property Details", font=("Microsoft Sans", 14), bg="mintcream")
            label1.grid(row=14, column=0, columnspan=5, sticky="n")  # property details LABEL

            label2 = Label(root, padx=100, text="Property Location", font=("Microsoft Sans", 14), bg="mintcream")
            label2.grid(row=18, column=0, columnspan=5, sticky="n")  # location LABEL
            radio_frame = Frame(root, bg="mintcream")

            def on_enter3(e):  # enter city
                city.delete(0, 'end')

            def on_leave3(e):
                if city.get() == '':
                    city.insert(0, 'Enter City')

            city = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                         font=('Microsoft Yahel UI Light', 11))
            city.place(x=350, y=480)
            city.insert(0, 'Enter City')
            city.bind("<FocusIn>", on_enter3)
            city.bind("<FocusOut>", on_leave3)

            Frame(root, width=295, height=2, bg="black").place(x=350, y=510)

            # ----------------------------------------------------------------------------------------

            def on_enter4(e):  # enter locality
                localty.delete(0, 'end')

            def on_leave4(e):
                if localty.get() == '':
                    localty.insert(0, 'Enter Locality')

            localty = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                            font=('Microsoft Yahel UI Light', 11))
            localty.place(x=350, y=540)
            localty.insert(0, 'Enter Locality')
            localty.bind("<FocusIn>", on_enter4)
            localty.bind("<FocusOut>", on_leave4)

            Frame(root, width=295, height=2, bg="black").place(x=350, y=570)
            radio_frame.grid(row=15, column=0, columnspan=5, sticky="n")

            # Use grid to arrange radio buttons horizontally
            x = IntVar()
            for index in range(len(vend2)):
                radiobutton = Radiobutton(
                    radio_frame,
                    text=vend2[index],
                    variable=x,
                    value=index,
                    padx=10,
                    font=("Microsoft Sans", 12))
                radiobutton.grid(row=3, column=index, padx=15, pady=30)
            submit_butt = Button(root, text="Save",
                                 font=('Bold', 15), bg='#B31312',
                                 fg='white', bd=1)
            submit_butt.place(relx=0.458, rely=0.9)
            frame1.place(relx=0.1, rely=0.25)

        def builder_function():
            frame1 = Frame(root,
                           width=600,
                           height=1000,
                           bg="mintcream",
                           relief=GROOVE)

            def on_enter6(e):
                enter_id.delete(0, 'end')

            def on_leave6(e):
                if enter_id.get() == '':
                    enter_id.insert(0, 'Enter Builder ID')

            enter_id = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                             font=('Microsoft Yahel UI Light', 11))
            enter_id.place(x=350, y=220)
            enter_id.insert(0, 'Enter Builder ID')
            enter_id.bind("<FocusIn>", on_enter6)
            enter_id.bind("<FocusOut>", on_leave6)

            Frame(root, width=295, height=2, bg="black").grid(row=10, column=0, padx=350, pady=80)
            submit_butt = Button(root, text="Save",
                                 font=('Bold', 15), bg='#B31312',
                                 fg='white', bd=1)
            submit_butt.place(relx=0.458, rely=0.9)
            label2 = Label(root, padx=100, text="Property Location", font=("Microsoft Sans", 14), bg="mintcream")
            label2.grid(row=18, column=0, columnspan=5, sticky="n")  # location LABEL

            def on_enter3(e):  # enter city
                city.delete(0, 'end')

            def on_leave3(e):
                if city.get() == '':
                    city.insert(0, 'Enter City')

            city = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                         font=('Microsoft Yahel UI Light', 11))
            city.place(x=350, y=380)
            city.insert(0, 'Enter City')
            city.bind("<FocusIn>", on_enter3)
            city.bind("<FocusOut>", on_leave3)

            Frame(root, width=295, height=2, bg="black").place(x=350, y=410)

            # ----------------------------------------------------------------------------------------

            def on_enter4(e):  # enter locality
                localty.delete(0, 'end')

            def on_leave4(e):
                if localty.get() == '':
                    localty.insert(0, 'Enter Locality')

            localty = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                            font=('Microsoft Yahel UI Light', 11))
            localty.place(x=350, y=440)
            localty.insert(0, 'Enter Locality')
            localty.bind("<FocusIn>", on_enter4)
            localty.bind("<FocusOut>", on_leave4)

            Frame(root, width=295, height=2, bg="black").place(x=350, y=470)

            def on_enter4(e):  # enter floors
                localty.delete(0, 'end')

            def on_leave4(e):
                if localty.get() == '':
                    localty.insert(0, 'Number of Floors')

            localty = Entry(root, width=25, fg='black', border=0, bg='mintcream',
                            font=('Microsoft Yahel UI Light', 11))
            localty.place(x=350, y=500)
            localty.insert(0, 'Number of Floors')
            localty.bind("<FocusIn>", on_enter4)
            localty.bind("<FocusOut>", on_leave4)

            Frame(root, width=295, height=2, bg="black").place(x=350, y=530)
            frame1.place(relx=0.1, rely=0.25)

        # -----------------------------------------------------------------------------------------------------------------------
        # Create a frame to contain the radio buttons
        radio_frame = Frame(root, bg="mintcream")
        radio_frame.grid(row=5, column=0, columnspan=5, sticky="n")

        ownerImage = PhotoImage(file='icons/ownership30.png')
        agentImage = PhotoImage(file='icons/real-estate-agent30.png')
        builderImage = PhotoImage(file='icons/builder30.png')
        sellerImages = [ownerImage, agentImage, builderImage]

        # Use grid to arrange radio buttons horizontally
        x = IntVar()
        for index in range(len(seller)):
            if index == 0:
                command = owner_function
            elif index == 1:
                # owner_function = False
                command = agent_function
            else:
                command = builder_function

            radiobutton = Radiobutton(
                radio_frame,
                text=seller[index],
                variable=x,
                value=index,
                padx=30,
                font=("Microsoft Sans", 12),
                image=sellerImages[index],
                compound='left',
                indicatoron=0,
                command=command
            )
            radiobutton.grid(row=3, column=index, padx=15)

root = Tk()
obj = sell1(root)
root.mainloop()




