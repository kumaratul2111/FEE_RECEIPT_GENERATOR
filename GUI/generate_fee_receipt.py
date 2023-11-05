import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def fee_receipt_generator() :
    # Create the main application window
    return_dict = {}
    app = tk.Tk()
    app.title("Fee Receipt Generator")

    # Set a custom background color
    app.configure(bg="#f2f2f2")

    # Get the screen dimensions
    win_width = app.winfo_screenwidth()
    win_height = app.winfo_screenheight()

    # Create a frame to hold the content and make it expand to fill the window
    content_frame = ttk.Frame(app)
    content_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Create and place labels and input fields with modern styling
    label_style = ttk.Style()
    label_style.configure("TLabel", font=("Helvetica", 14), foreground="black")
    entry_style = ttk.Style()
    entry_style.configure("TEntry", font=("Helvetica", 14), foreground="black", width=30)  # Increased field width

    # Define a list of available years (customize as needed)
    available_years = [str(year) for year in range(2020, 2031)]  # Example: 2020 to 2030

    # Create and style the Combobox for the "Year" field
    year_label = ttk.Label(content_frame, text="Year:")
    year_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    year_var = tk.StringVar()
    year_combobox = ttk.Combobox(content_frame, textvariable=year_var, values=available_years, state="readonly")
    year_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    year_combobox.set("Select Year")


    # Define a list of available months
    available_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Create and style the Combobox for the "Month" field
    month_label = ttk.Label(content_frame, text="Month:")
    month_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    month_var = tk.StringVar()
    month_combobox = ttk.Combobox(content_frame, textvariable=month_var, values=available_months, state="readonly")
    month_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    month_combobox.set("Select Month")

    # Define a list of available classes
    available_classes = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8"]

    # Create and style the Combobox (dropdown) for the "Class" field
    class_label = ttk.Label(content_frame, text="Class:")
    class_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    class_var = tk.StringVar()
    class_combobox = ttk.Combobox(content_frame, textvariable=class_var, values=available_classes, state="readonly")
    class_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    class_combobox.set("Select Class")

    # Define tuition_fee_var and create the entry widget for the "Tuition Fee" field
    tuition_fee_label = ttk.Label(content_frame, text="Tuition Fee:")
    tuition_fee_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    tuition_fee_var = tk.DoubleVar()
    tuition_fee_entry = ttk.Entry(content_frame, textvariable=tuition_fee_var, style="TEntry")
    tuition_fee_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    # Define hostel_fee_var and create the entry widget for the "Hostel Fee" field
    hostel_fee_label = ttk.Label(content_frame, text="Hostel Fee:")
    hostel_fee_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    hostel_fee_var = tk.DoubleVar()
    hostel_fee_entry = ttk.Entry(content_frame, textvariable=hostel_fee_var, style="TEntry")
    hostel_fee_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Define mess_fee_var and create the entry widget for the "Mess Fee" field
    mess_fee_label = ttk.Label(content_frame, text="Mess Fee:")
    mess_fee_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    mess_fee_var = tk.DoubleVar()
    mess_fee_entry = ttk.Entry(content_frame, textvariable=mess_fee_var, style="TEntry")
    mess_fee_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

    # Define transportation_fee_var and create the entry widget for the "Transportation Fee" field
    transportation_fee_label = ttk.Label(content_frame, text="Transportation Fee:")
    transportation_fee_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
    transportation_fee_var = tk.DoubleVar()
    transportation_fee_entry = ttk.Entry(content_frame, textvariable=transportation_fee_var, style="TEntry")
    transportation_fee_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    # Define other_fee_var and create the entry widget for the "Other Fee" field
    other_fee_label = ttk.Label(content_frame, text="Other Fee:")
    other_fee_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
    other_fee_var = tk.DoubleVar()
    other_fee_entry = ttk.Entry(content_frame, textvariable=other_fee_var, style="TEntry")
    other_fee_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    # Create and style the Submit button
    submit_button = ttk.Button(content_frame, text="Submit", command=app.destroy, style="TButton")
    submit_button.grid(row=8, columnspan=2, padx=10, pady=10)

    # Create a custom style for the button with a modern look
    button_style = ttk.Style()
    button_style.configure("TButton", font=("Helvetica", 14, "bold"), foreground="white", background="green")

    # Configure row and column weights to make the content frame expand to fill the window
    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Start the main GUI loop
    app.mainloop()
    
    #Reading the variables
    year = year_var.get()
    month = month_var.get()
    class_name = class_var.get()
    tuition_fee = tuition_fee_var.get()
    hostel_fee = hostel_fee_var.get()
    mess_fee = mess_fee_var.get()
    transportation_fee = transportation_fee_var.get()
    other_fee = other_fee_var.get()

    #Adding variables to dictionary to be returned
    return_dict['year'] = year
    return_dict['month'] = month
    return_dict['class_name'] = class_name
    return_dict['tuition_fee'] = tuition_fee
    return_dict['hostel_fee'] = hostel_fee
    return_dict['mess_fee'] = mess_fee
    return_dict['transportation_fee'] = transportation_fee
    return_dict['other_fee'] = other_fee

    #Printing the values
    print("Data saved to variables")
    print(f"Year: {year}")
    print(f"Month: {month}")
    print(f"class name: {class_name}")
    print(f"Tution Fee: {tuition_fee }")
    print(f"Hostel Fee: {hostel_fee }")
    print(f"Hostel Fee: {hostel_fee }")
    print(f"Mess Fee: {mess_fee}")
    print(f"Transporation Fee: {transportation_fee }")
    print(f"Other Fee: {other_fee }")

    return  return_dict

