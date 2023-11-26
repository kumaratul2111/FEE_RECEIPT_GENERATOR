import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
import subprocess
import update_database
import send_email
import fee_pdf
import payment_pdf


def show_frame(frame):
    frame.tkraise()
# This function takes input from GUI and show a bar plot of the requested data.
def analysis():

    l3 = {}
    l3['year'] = year_var3.get()
    l3['month'] = month_var3.get()
    l3['class_name'] = class_var3.get()

    print(l3)
    categories = []
    DUES = []
    PAYMENT = []
    rows = update_database.fetch_details_for_a_class(l3['class_name'], l3['month'], l3['year'])
    print(rows)
    for row in rows :
        categories.append(row[0])
        PAYMENT.append(row[1])
        DUES.append(row[2])
    print(categories)
    print(PAYMENT)
    print(DUES)

    bar_width = 0.35

    # Create positions for the bars
    bar_positions_set1 = np.arange(len(categories))
    bar_positions_set2 = bar_positions_set1 + bar_width

    # Create bar plots for both sets of data
    plt.bar(bar_positions_set1, PAYMENT, width=bar_width, label='Payment', color='blue')
    plt.bar(bar_positions_set2, DUES, width=bar_width, label='Dues', color='orange')

    # Adding labels and title
    plt.xlabel('Student')
    plt.ylabel('Dues and Payment')
    plt.title('Payment for the month of ' + l3['month'] + l3['class_name'])
    plt.xticks(bar_positions_set1 + bar_width / 2, categories)  # Set category labels at the center of the grouped bars
    plt.legend()  # Display legend

    # Display the plot
    plt.show()

    # # Open a new window to show the success message
    # success_window = tk.Toplevel(root)
    # success_window.title("Success")

    # # Create a label to display the success message
    # success_label = tk.Label(success_window, text="Bar Plot Generated Successfully !", font=("Helvetica", 20))
    # success_label.pack(padx=20, pady=20)

# This function takes input from GUI and create fee receipts for all students in a class. It also send the receipts as email attachment.
def fee_receipt_generator():
   
    l1 = {}
    l1['year'] = year_var1.get()
    l1['month'] = month_var1.get()
    l1['class_name'] = class_var1.get()
    l1['tuition_fee'] = tuition_fee_var.get()
    l1['hostel_fee'] = hostel_fee_var.get()
    l1['mess_fee'] = mess_fee_var.get()
    l1['transportation_fee'] = transportation_fee_var.get()
    l1['other_fee'] = other_fee_var.get()
    
    # l = GUI.generate_fee_receipt.fee_receipt_generator()
    print("main", l1, type(l1))
    update_database.update_tuition_fee(l1['class_name'], l1['tuition_fee'], l1['month'], l1['year'])
    update_database.update_hostel_fee(l1['class_name'], l1['hostel_fee'], l1['month'], l1['year'])
    update_database.update_transportation_fee(l1['class_name'], l1['transportation_fee'], l1['month'], l1['year'])
    update_database.update_mess_fee(l1['class_name'], l1['mess_fee'], l1['month'], l1['year'])
    update_database.update_other_fee(l1['class_name'], l1['other_fee'], l1['month'], l1['year'])
    update_database.update_remaining_dues(l1['class_name'], l1['month'], l1['year'])
    rows = update_database.fetch_details(l1['class_name'], l1['month'], l1['year'])
    print(l1['month'], l1['year'])
    for row in rows :
        fee_pdf.create_fee_pdf(row)
        print(row)
        send_email.send_email(row, l1['month'], l1['year'])
    

    # Open a new window to show the success message
    success_window = tk.Toplevel(root)
    success_window.title("Success")

    # Create a label to display the success message
    success_label = tk.Label(success_window, text="Fee Generated successfully and email sent!! ", font=("Helvetica", 20))
    success_label.pack(padx=20, pady=20)


# This function takes input from GUI and record payment for a student.
def payment_recorder() :

    l2 = {}
    l2['year'] = year_var2.get()
    l2['month'] = month_var2.get()
    l2['class_name'] = class_var2.get()
    l2['payment'] = payment_var.get()
    l2['roll'] = roll_var.get()

    # l2 = GUI.record_payment.payment_recorder()
    print("main", l2)
    update_database.record_payment_table(l2['class_name'], l2['payment'], l2['month'], l2['year'], l2['roll'])
    rows = update_database.fetch_details_of_a_student(l2['class_name'], l2['month'], l2['year'], l2['roll'])
    for row in rows :
        payment_pdf.create_payment_pdf(row, l2['payment'])
        print(row)
        send_email.send_email(row, l2['month'], l2['year'])

    #year.delete(0, tk.END)
    #month.delete(0, tk.END)
    #class_name.delete(0, tk.END)
    #payment.delete(0, tk.END)
    #roll.delete(0, tk.END)


    # Open a new window to show the success message
    success_window = tk.Toplevel(root)
    success_window.title("Success")

    # Create a label to display the success message
    success_label = tk.Label(success_window, text="Payment recorded !! ", font=("Helvetica", 20))
    success_label.pack(padx=20, pady=20)



# Create the main window
root = tk.Tk()
root.title("Tabbed GUI")
root.geometry("1080x1080")
root.configure(background="#000000")

# Create a Notebook (Tabbed container)
notebook = ttk.Notebook(root, style='TNotebook')

# Configure style for the notebook
style = ttk.Style()
style.configure('TNotebook', padding=[20, 20])

# Configure style for the tab buttons
style.configure('TNotebook.Tab', background='#aaa', foreground='black', font=('Helvetica', 15), padding=[10, 2])


# Frame for the first tab
tab1_frame = ttk.Frame(notebook)
notebook.add(tab1_frame, text="Visualization")

# Frame for the second tab
tab2_frame = ttk.Frame(notebook)
notebook.add(tab2_frame, text="Generate Fee")

# Frame for the third tab
tab3_frame = ttk.Frame(notebook)
notebook.add(tab3_frame, text="Record payment")


#==============================================================***Frame1================================================================================
# Add content to Tab 1
tab1_label = tk.Label(tab1_frame, text="Create bar plots", font=("Helvetica", 20, 'bold'), fg='black')
# tab1_label.pack(padx=10, pady=20)
tab1_label.grid(row=0, column=1, padx=10, pady=50, sticky="w")

# Widgets from the second GUI directly added to tab1_frame
label_color = "#ecf0f1"  # Light Gray
button_color = "#2ecc71"  # Green

class_label3 = tk.Label(tab1_frame, text="Class:", font=("Helvetica", 20))
class_label3.grid(row=1, column=0, padx=10, pady=10, sticky="w")
month_label3 = tk.Label(tab1_frame, text="Month:", font=("Helvetica", 20))
month_label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
year_label3 = tk.Label(tab1_frame, text="Year:", font=("Helvetica", 20))
year_label3.grid(row=3, column=0, padx=10, pady=10, sticky="w")


available_classes = ["Class1", "Class2", "Class3", "Class4", "Class5", "Class6", "Class7", "Class8"]
class_var3 = tk.StringVar()
class_combobox = ttk.Combobox(tab1_frame, textvariable=class_var3, values=available_classes, state="readonly", font=("Helvetica", 15,))
class_combobox.grid(row=1, column=2, padx=10, pady=10, sticky="w")
class_combobox.set("Select Class")

available_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_var3 = tk.StringVar()
month_combobox = ttk.Combobox(tab1_frame, textvariable=month_var3, values=available_months, state="readonly", font=("Helvetica", 15))
month_combobox.grid(row=2, column=2, padx=10, pady=10, sticky="w")
month_combobox.set("Select Month")

available_years = [str(year) for year in range(2020, 2031)] 
year_var3 = tk.StringVar()
year_combobox = ttk.Combobox(tab1_frame, textvariable=year_var3, values=available_years, state="readonly", font=("Helvetica", 15))
year_combobox.grid(row=3, column=2, padx=10, pady=10, sticky="w")
year_combobox.set("Select Year")


record_button = tk.Button(tab1_frame, text="Submit", command=analysis, bg=button_color, fg=label_color)
record_button.grid(row=4, column=2, pady=50)

# Create a custom style for the button with a modern look
# button_style = ttk.Style()
# button_style.configure("TButton", font=("Helvetica", 14, "bold"), foreground="white", background="green")

#===========================================================**Frame2================================================================================================
# Add content to Tab 2
tab2_label = tk.Label(tab2_frame, text="Generate Fee for an entire class", font=("Helvetica", 20, 'bold'), fg='black')
tab2_label.grid(row=0, column=1, padx=10, pady=50, sticky="w")

# Widgets for the "Year" field under tab2_frame
year_label = ttk.Label(tab2_frame, text="Year", font=("Helvetica", 15))
year_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Define a list of available years (customize as needed)
available_years = [str(year) for year in range(2020, 2031)] 

# Widgets for the "Year" field under tab2_frame
year_var1 = tk.StringVar()
year_combobox = ttk.Combobox(tab2_frame, textvariable=year_var1, values=available_years, state="readonly", font=("Helvetica", 15))
year_combobox.grid(row=1, column=2, padx=10, pady=10, sticky="w")
year_combobox.set("Select Year")



# Widgets for the "Month" field under tab2_frame
month_label = ttk.Label(tab2_frame, text="Month", font=("Helvetica", 15))
month_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

#Define a list of available months
available_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_var1 = tk.StringVar()
month_combobox = ttk.Combobox(tab2_frame, textvariable=month_var1, values=available_months, state="readonly", font=("Helvetica", 15))
month_combobox.grid(row=2, column=2, padx=10, pady=10, sticky="w")
month_combobox.set("Select Month")



# Widgets for the "Class" field under tab2_frame
class_label = tk.Label(tab2_frame, text="Class", font=("Helvetica", 15))
class_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Define a list of available classes
available_classes = ["Class1", "Class2", "Class3", "Class4", "Class5", "Class6", "Class7", "Class8"]
class_var1 = tk.StringVar()
class_combobox = ttk.Combobox(tab2_frame, textvariable=class_var1, values=available_classes, state="readonly", font=("Helvetica", 15,))
class_combobox.grid(row=3, column=2, padx=10, pady=10, sticky="w")
class_combobox.set("Select Class")



# Define tuition_fee_var and create the entry widget for the "Tuition Fee" field
tuition_fee_label = ttk.Label(tab2_frame, text="Tuition Fee", font=("Helvetica", 15))
tuition_fee_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

tuition_fee_var = tk.DoubleVar()
tuition_fee_entry = ttk.Entry(tab2_frame, textvariable=tuition_fee_var, style="TEntry", font=("Helvetica", 15))
tuition_fee_entry.grid(row=4, column=2, padx=10, pady=10, sticky="w")



# Define hostel_fee_var and create the entry widget for the "Hostel Fee" field
hostel_fee_label = ttk.Label(tab2_frame, text="Hostel Fee", font=("Helvetica", 15))
hostel_fee_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

hostel_fee_var = tk.DoubleVar()
hostel_fee_entry = ttk.Entry(tab2_frame, textvariable=hostel_fee_var, style="TEntry", font=("Helvetica", 15))
hostel_fee_entry.grid(row=5, column=2, padx=10, pady=10, sticky="w")



# Define mess_fee_var and create the entry widget for the "Mess Fee" field
mess_fee_label = ttk.Label(tab2_frame, text="Mess Fee", font=("Helvetica", 15))
mess_fee_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

mess_fee_var = tk.DoubleVar()
mess_fee_entry = ttk.Entry(tab2_frame, textvariable=mess_fee_var, style="TEntry", font=("Helvetica", 15))
mess_fee_entry.grid(row=6, column=2, padx=10, pady=10, sticky="w")


# Define transportation_fee_var and create the entry widget for the "Transportation Fee" field
transportation_fee_label = ttk.Label(tab2_frame, text="Transportation Fee:", font=("Helvetica", 15))
transportation_fee_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")

transportation_fee_var = tk.DoubleVar()
transportation_fee_entry = ttk.Entry(tab2_frame, textvariable=transportation_fee_var, style="TEntry", font=("Helvetica", 15))
transportation_fee_entry.grid(row=7, column=2, padx=10, pady=10, sticky="w")

# Define other_fee_var and create the entry widget for the "Other Fee" field
other_fee_label = ttk.Label(tab2_frame, text="Other Fee:", font=("Helvetica", 15))
other_fee_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

other_fee_var = tk.DoubleVar()
other_fee_entry = ttk.Entry(tab2_frame, textvariable=other_fee_var, style="TEntry", font=("Helvetica", 15))
other_fee_entry.grid(row=8, column=2, padx=10, pady=10, sticky="w")

# Create and style the Submit button
submit_button = ttk.Button(tab2_frame, text="Submit", command=fee_receipt_generator, style="TButton")
submit_button.grid(row=9, column=2, pady=50)

# Create a custom style for the button with a modern look
button_style = ttk.Style()
button_style.configure("TButton", font=("Helvetica", 14, "bold"), foreground="white", background="green")




#============================================================Frame3============================================================
# Add content to Tab 3
tab3_label = tk.Label(tab3_frame, text="Record Payment for a Student", font=("Helvetica", 20, 'bold'), fg='black')
tab3_label.grid(row=0, column=1, padx=10, pady=50, sticky="w")

# Widgets for the "Year" field under tab3_frame
year_label = ttk.Label(tab3_frame, text="Year:", font=("Helvetica", 15))
# year_label.grid(row=0, column=0)
year_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

year_var2 = tk.StringVar()
year_combobox = ttk.Combobox(tab3_frame, textvariable=year_var2, values=available_years, state="readonly", font=("Helvetica", 15))
year_combobox.grid(row=1, column=2, padx=10, pady=10, sticky="w")
year_combobox.set("Select Year")

#year_combobox.bind("<<ComboboxSelected>>", payment_recorder)

# Widgets for the "Month" field under tab3_frame
month_label = ttk.Label(tab3_frame, text="Month:", font=("Helvetica", 15))
month_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

month_var2 = tk.StringVar()
month_combobox = ttk.Combobox(tab3_frame, textvariable=month_var2, values=available_months, state="readonly", font=("Helvetica", 15))
month_combobox.grid(row=2, column=2, padx=10, pady=10, sticky="w")
month_combobox.set("Select Month")

# Widgets for the "Class" field under tab3_frame
class_label = ttk.Label(tab3_frame, text="Class:", font=("Helvetica", 15))
class_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

class_var2 = tk.StringVar()
class_combobox = ttk.Combobox(tab3_frame, textvariable=class_var2, values=available_classes, state="readonly", font=("Helvetica", 15))
class_combobox.grid(row=3, column=2, padx=10, pady=10, sticky="w")
class_combobox.set("Select Class")

# Widgets for the "Roll" field under tab3_frame
roll_label = ttk.Label(tab3_frame, text="Roll:", font=("Helvetica", 15))
roll_label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

roll_var = tk.StringVar()
roll_entry = ttk.Entry(tab3_frame, textvariable=roll_var, style="TEntry", font=("Helvetica", 15))
roll_entry.grid(row=4, column=2, padx=10, pady=10, sticky="w")

# Widgets for the "Payment" field under tab3_frame
payment_label = ttk.Label(tab3_frame, text="Payment:", font=("Helvetica", 15))
payment_label.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

payment_var = tk.DoubleVar()
payment_entry = ttk.Entry(tab3_frame, textvariable=payment_var, style="TEntry", font=("Helvetica", 15))
payment_entry.grid(row=5, column=2, padx=10, pady=10, sticky="w")

# Create and style the Submit button under tab3_frame
submit_button = ttk.Button(tab3_frame, text="Submit", command=payment_recorder, style="TButton")
submit_button.grid(row=6, column=2, pady=50)

# Create a custom style for the button with a modern look
button_style = ttk.Style()
button_style.configure("TButton", font=("Helvetica", 14, "bold"), foreground="white", background="green")



# Pack the Notebook
notebook.pack(expand=True, fill="both")

# Run the Tkinter event loop
root.mainloop()
