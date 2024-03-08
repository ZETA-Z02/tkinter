import tkinter as tk
from tkinter import messagebox
from LoginInterface import LoginInterface, User


class LoginApp:
    def __init__(self, master):
        self.master = master
        self.login_interface = LoginInterface()
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.master.title("Login")

        # Set the window size and background color
        self.master.geometry("300x200")
        self.master.configure(bg="#008080")

        # Create and add username label
        username_label = tk.Label(self.master, text="Username:", bg="#008080")
        username_label.grid(row=0, column=0, sticky=tk.W)

        # Create and add username entry
        username_entry = tk.Entry(self.master, textvariable=self.username)
        username_entry.grid(row=0, column=1)

        # Create and add password label
        password_label = tk.Label(self.master, text="Password:", bg="#008080")
        password_label.grid(row=1, column=0, sticky=tk.W)

        # Create and add password entry
        password_entry = tk.Entry(self.master, textvariable=self.password)
        password_entry.grid(row=1, column=1)

        # Create and add login button
        login_button = tk.Button(
            self.master, text="Login", command=self.login, bg="#008080", fg="white")
        login_button.grid(row=2, column=0, columnspan=2)

        # Create and add register button
        register_button = tk.Button(
            self.master, text="Register", command=self.register, bg="#008080", fg="white")
        register_button.grid(row=3, column=0, columnspan=2)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        result = self.login_interface.login(username, password)
        if result == "Logged in successfully.":
            messagebox.showinfo("Login", "Logged in successfully.")
        else:
            messagebox.showerror("Login", result)

    def register(self):
        username = self.username.get()
        password = self.password.get()
        result = self.login_interface.register(username, password)
        if result == "User created successfully.":
            messagebox.showinfo("Register", "User created successfully.")
        else:
            messagebox.showerror("Register", result)


def main():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
