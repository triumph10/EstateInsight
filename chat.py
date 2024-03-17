from tkinter import *
from tkinter import ttk
from socket import *
from threading import *

class MainInterface:
    def __init__(self, root):
        self.root = root
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
        self.root.iconphoto(True, self.icon)




        # Call method to set up chat interface
        self.setup_chat_interface()

    def buy(self):
        self.root.destroy()
        import buy1

    def home(self):
        self.root.destroy()
        import maininterface

    def rent(self):
        self.root.destroy()
        import Rent1

    def setup_chat_interface(self):
        chat_frame = Frame(self.root)
        chat_frame.pack(fill=BOTH, expand=True)  # Fill the entire window
        chat_frame.grid_columnconfigure(0, weight=1)
        chat_frame.grid_rowconfigure(0, weight=1)

        self.chat_text = Text(chat_frame, wrap=WORD, highlightbackground='gray', highlightcolor='black')
        self.chat_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.message_entry = Entry(chat_frame, highlightbackground='gray', highlightcolor='black')
        self.message_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        send_button = Button(chat_frame, text="Send", command=self.send_message, bd=1)
        send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # setting up the back page button

        back_button = Button(chat_frame, bg='#B31312', fg='white', text='<<Back')
        back_button.place(relx=0.94, rely=0.1)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.chat_text.insert(END, f"You: {message}\n")
            self.message_entry.delete(0, END)
            # Send the message to the server here

    def start_server(self):
        host_ip = "0.0.0.0"  # Change this to your desired host IP
        port_number = 777

        def client_thread():
            client_socket = socket(AF_INET, SOCK_STREAM)
            client_socket.connect((host_ip, port_number))
            # Your client-side code here

        def server_thread():
            host_socket = socket(AF_INET, SOCK_STREAM)
            host_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            host_socket.bind((host_ip, port_number))
            host_socket.listen()

            clients = set()

            while True:
                client_socket, client_address = host_socket.accept()
                clients.add(client_socket)
                print("Connection established with:", client_address[0] + ":" + str(client_address[1]))
                thread = Thread(target=self.client_handler, args=(client_socket, client_address, clients))
                thread.start()

        server = Thread(target=server_thread)
        client = Thread(target=client_thread)

        server.start()
        client.start()

    def client_handler(self, client_socket, client_address, clients):
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            print(client_address[0] + ":" + str(client_address[1]) + " says: " + message)
            for client in clients:
                if client is not client_socket:
                    client.send(
                        (client_address[0] + ":" + str(client_address[1]) + " says: " + message).encode("utf-8"))

            if not message:
                clients.remove(client_socket)
                print(client_address[0] + ":" + str(client_address[1]) + " disconnected")
                break

        client_socket.close()

if __name__ == "__main__":
    root = Tk()
    obj = MainInterface(root)
    root.mainloop()
