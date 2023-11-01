import tkinter as tk
from tkinter import ttk

# Declare global variables
entry_name = None
entry_last_name = None
entry_email = None
entry_mobile = None
entry_password = None
entry_confirm_password = None

def register_button_click():
    # Create a new window for user registration
    registration_window = tk.Toplevel(screen)
    registration_window.iconbitmap('images/W.ico')
    registration_window.title("User Registration")

    # Create and configure registration form widgets
    label_name = ttk.Label(registration_window, text="First Name:")
    label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    global entry_name
    entry_name = ttk.Entry(registration_window)
    entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    label_last_name = ttk.Label(registration_window, text="Last Name:")
    label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    global entry_last_name
    entry_last_name = ttk.Entry(registration_window)
    entry_last_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    label_email = ttk.Label(registration_window, text="Email:")
    label_email.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    global entry_email
    entry_email = ttk.Entry(registration_window)
    entry_email.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    label_mobile = ttk.Label(registration_window, text="Mobile:")
    label_mobile.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    global entry_mobile
    entry_mobile = ttk.Entry(registration_window)
    entry_mobile.grid(row=3, column=1, padx=10, pady=5, sticky="w")

    label_password = ttk.Label(registration_window, text="Password:")
    label_password.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    global entry_password
    entry_password = ttk.Entry(registration_window, show="*")
    entry_password.grid(row=4, column=1, padx=10, pady=5, sticky="w")

    label_confirm_password = ttk.Label(registration_window, text="Confirm Password:")
    label_confirm_password.grid(row=5, column=0, padx=10, pady=5, sticky="e")
    global entry_confirm_password
    entry_confirm_password = ttk.Entry(registration_window, show="*")
    entry_confirm_password.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    register_button = ttk.Button(registration_window, text="Register", command=collect_registration_data)
    register_button.grid(row=6, column=1, padx=10, pady=10)

def collect_registration_data():
    # Retrieve user data from the registration form
    first_name = entry_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    mobile = entry_mobile.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    # You can now use these variables to do whatever you want with the user data
    # For example, you can print them to the console
    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Email:", email)
    print("Mobile:", mobile)
    print("Password:", password)
    print("Confirm Password:", confirm_password)

def login_button_click():
    # Create a new window for user registration
    login_window = tk.Toplevel(screen)
    login_window.iconbitmap('images/W.ico')
    login_window.title("User Login")

    label_email = ttk.Label(login_window, text="Email:")
    label_email.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_email = ttk.Entry(login_window)
    entry_email.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    label_password = ttk.Label(login_window, text="Password:")
    label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_password = ttk.Entry(login_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    login_button = ttk.Button(login_window, text="Login")
    login_button.grid(row=2, column=1, padx=10, pady=10)

def make_responsive(frame):
    # Configure row and column weights to make the frame expand
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    # Create a registration button with rounded border
    register_button = tk.Button(frame, text="Registration", command=register_button_click, width=20, height=2, relief=tk.RAISED, borderwidth=2)
    register_button.grid(row=0, column=0, padx=10, pady=30, sticky="nsew")

    # Create a login button with rounded border
    login_button = tk.Button(frame, text="Login", command=login_button_click, width=20, height=2, relief=tk.RAISED, borderwidth=2)
    login_button.grid(row=0, column=1, padx=10, pady=30, sticky="nsew")

screen = tk.Tk()
screen.title("Welcare-Laboratory")
screen.geometry('500x500')
screen.iconbitmap('images/W.ico')

# Load your logo image and resize it to 150x100 pixels
logo_image = tk.PhotoImage(file="images/logo.png")
logo_image = logo_image.subsample(10)

# Create a label to display the logo
logo_label = tk.Label(screen, image=logo_image)
logo_label.pack(fill="both", expand=True)

# Create a Frame for the buttons
button_frame = tk.Frame(screen)
button_frame.pack(fill="both", expand=True)
make_responsive(button_frame)

screen.mainloop()
