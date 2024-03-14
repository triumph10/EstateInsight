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
                    height=5)
        one.pack(fill=X, side=TOP)
        insertButt = Button(one,
                            text="Login",
                            bg="#B31312",
                            fg="white",
                            border=0,
                            activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=3, pady=2)
        insertButt = Button(one,
                            text="Sign Up",
                            bg="#B31312",
                            fg="white",
                            border=0,
                            activebackground='#B67352')
        insertButt.pack(side=RIGHT, padx=3, pady=2)

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

        # setting up the toolbar for the app
        toolbar = Frame(root, bg="white", relief=GROOVE, bd=1, pady=2)

        printButt = Button(toolbar,
                           text="Home",
                           bg="white",
                           border=0,
                           activebackground='#B67352', command=self.home)
        printButt.pack(side=LEFT, padx=20, pady=2)
        insertButt = Button(toolbar,
                            text="Buy",
                            bg="white",
                            border=0,
                            activebackground='#B67352',
                            command=self.buy)
        insertButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Sell",
                           bg="white",
                           border=0,
                           activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Rent",
                           bg="white",
                           border=0,
                           activebackground='#B67352', command=self.rent)
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Wishlist",
                           bg="white",
                           border=0,
                           activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)
        printButt = Button(toolbar,
                           text="Help",
                           bg="white",
                           border=0,
                           activebackground='#B67352')
        printButt.pack(side=LEFT, padx=20, pady=2)

        toolbar.pack(side=TOP, fill=X)

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

        self.chat_text = Text(chat_frame, wrap=WORD)
        self.chat_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.message_entry = Entry(chat_frame)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        send_button = Button(chat_frame, text="Send", command=self.send_message)
        send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

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
