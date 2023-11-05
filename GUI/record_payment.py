import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

def record_payment():
    student_roll = roll_entry.get()
    payment_amount = payment_entry.get()
    
    # You can process and record the payment here
    # For this example, we'll just print the values
    print(f"Student Roll: {student_roll}")
    print(f"Payment Amount: {payment_amount}")

    
     # Clear the entry fields by updating them with empty strings
    roll_entry.delete(0, tk.END)
    payment_entry.delete(0, tk.END)
    
    # Open a new window to show the success message
    success_window = tk.Toplevel(root)
    success_window.title("Success")

    # Create a label to display the success message
    success_label = tk.Label(success_window, text="Payment Recorded Successfully!", font=("Helvetica", 20))
    success_label.pack(padx=20, pady=20)

def payment_recorder() :
    # Create the main window
    root = tk.Tk()
    root.title("Payment Record")

    # Get the screen dimensions
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()

    # Set the window size to match the screen dimensions
    root.geometry(f"{win_width}x{win_height}")



    # Resize the image to fit the window
    # img = img.resize((win_width, win_height))

    # Create a PhotoImage from the resized image
    # bg_image = ImageTk.PhotoImage(img)
    # bg_label = tk.Label(root, image=bg_image)
    # bg_label.place(relwidth=1, relheight=1)

    # Set a custom color scheme
    label_color = "#ecf0f1"  # Light Gray
    button_color = "#2ecc71"  # Green
    roll_color="black" # Red
    # Create labels
    roll_label = tk.Label(root, text="Student Roll:", bg=roll_color, fg=label_color, font=("Helvetica", 20))
    payment_label = tk.Label(root, text="Payment:", bg=roll_color, fg=label_color, font=("Helvetica", 20))

    # Create entry fields
    roll_entry = tk.Entry(root, font=("Helvetica", 20))
    payment_entry = tk.Entry(root, font=("Helvetica", 20))

    # Create the record button
    record_button = tk.Button(root, text="Record", command=record_payment, bg=button_color, fg=label_color)

    # Center the labels and button by making them span multiple columns
    roll_label.grid(row=0, column=0, padx=10, pady=10, columnspan=4, sticky="e")
    payment_label.grid(row=1, column=0, padx=10, pady=10, columnspan=4, sticky="e")
    roll_entry.grid(row=0, column=4, padx=10, pady=10, columnspan=4, sticky="w")
    payment_entry.grid(row=1, column=4, padx=10, pady=10, columnspan=4, sticky="w")
    record_button.grid(row=2, column=0, padx=10, pady=10, columnspan=8)

    # Start the main event loop
    root.mainloop()
