import tkinter as tk
from tkinter import messagebox
import random

# Define the list of common passwords to check against
common_passwords = ["123456", "password", "123456789", "12345678", "12345"]

# Define the AI-based cyber security solution
def check_password(password):
    # Generate a random number between 1 and 10
    ai_decision = random.randint(1, 10)
    if password in common_passwords:
        # If the password is a common one, always reject it
        return False, "This password is too common. Please choose a different one."
    elif len(password) < 6:
        # If the password is too short, reject it
        return False, "This password is too short. Please choose a longer one."
    elif ai_decision <= 8:
        # If the AI decides that the password is secure, accept it
        return True, "Password accepted."
    else:
        # If the AI decides that the password is not secure, reject it
        return False, "This password is not secure. Please choose a different one."

# Define the function to validate the password and display the result
def validate_password():
    password = password_entry.get()
    is_secure, message = check_password(password)
    if is_secure:
        messagebox.showinfo("Password Validation", message)
    else:
        messagebox.showwarning("Password Validation", message)

# Create the main application window
root = tk.Tk()
root.geometry("600x400")  # Set the size of the root window to 600x400 pixels
root.title("AI Cyber Security Solution")

# Create a label and entry widget for the password
password_label = tk.Label(root, text="Enter a password:")
password_entry = tk.Entry(root, show="*")

# Create a button to validate the password
validate_button = tk.Button(root, text="Validate", command=validate_password)

# Pack the widgets into the window
password_label.pack(pady=10)
password_entry.pack(pady=10)
validate_button.pack(pady=10)

# Start the main event loop
root.mainloop()