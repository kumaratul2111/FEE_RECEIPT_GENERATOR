import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def Fee_receipt_generator_clicked() :
    global val
    global root
    val = 1
    root.destroy()

def Payment_Recorder_clicked() :
    global val
    global root
    val = 2
    root.destroy()

def Visualisations_clicked() :
    global val
    global root
    val = 3
    root.destroy()

def Exit_clicked() :
    global val
    global root
    val = 4
    root.destroy()
    
def input_choice() :
    # Create the main application window
    global root
    return_dict = {}
    root = tk.Tk()
    root.title("Choose Options")

    # Set a custom background color
    root.configure(bg="#f2f2f2")

    # Get the screen dimensions
    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()

    # Create a frame to hold the content and make it expand to fill the window
    content_frame = ttk.Frame(root)
    content_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Create and style the Submit button
    submit_button1 = ttk.Button(content_frame, text="Fee_receipt_generator", command=Fee_receipt_generator_clicked, style="TButton")
    submit_button1.grid(row=1, columnspan=2, padx=10, pady=10)

    submit_button2 = ttk.Button(content_frame, text="Payment_Recorder", command=Payment_Recorder_clicked, style="TButton")
    submit_button2.grid(row=2, columnspan=2, padx=10, pady=10)

    submit_button3 = ttk.Button(content_frame, text="Visualisations", command=Visualisations_clicked, style="TButton")
    submit_button3.grid(row=3, columnspan=2, padx=10, pady=10)

    submit_button4 = ttk.Button(content_frame, text="Exit", command=Exit_clicked, style="TButton")
    submit_button4.grid(row=4, columnspan=2, padx=10, pady=10)

    # Create a custom style for the button with a modern look
    button_style = ttk.Style()
    button_style.configure("TButton", font=("Helvetica", 14, "bold"), foreground="white", background="green")

    # Configure row and column weights to make the content frame expand to fill the window
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Start the main GUI loop
    root.mainloop()
