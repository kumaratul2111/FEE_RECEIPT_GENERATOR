import subprocess
# from jinja2 import Template  # You may need to install the Jinja2 library
def create_fee_pdf(row) :
    STUDENT_NAME = row[0]
    ROLL_NUMBER = row[2]
    CLASS_NAME = row[3]
    TUITION_FEE = row[4]
    MESS_FEE = row[6]
    HOSTEL_FEE= row[5]
    TRANSPORTATION_FEE= row[7]
    OTHER_FEE= row[8]
    TOTAL_AMOUNT = row[4] + row[5] + row[6] + row[7] + row[8]
    REMAINING_DUES = row[9]

    latex_content = f"""
    \\documentclass{{article}}
    \\usepackage[utf8]{{inputenc}}

    \\title{{Fee Receipt}}
    \\author{{}}
    \\date{{}}

    \\begin{{document}}

    \\maketitle

    \\section{{Student Information}}
    \\begin{{tabular}}{{ll}}
        \\textbf{{Name:}} & {{{STUDENT_NAME}}} \\\\
        \\textbf{{Roll Number:}} & {{{ROLL_NUMBER}}} \\\\ 
        \\textbf{{Class:}} & {{{CLASS_NAME}}} \\\\
    \\end{{tabular}}

    \\section{{Fee Details}}
    \\begin{{tabular}}{{|l|r|}}
        \\hline
        \\textbf{{Description}} & \\textbf{{Amount}} \\\\
        \\hline
        Tuition Fee & {{{TUITION_FEE}}} \\\\
        Hostel Fee & {{{HOSTEL_FEE}}} \\\\
        Mess fee & {{{MESS_FEE}}} \\\\
        Transportation Fee & {{{TRANSPORTATION_FEE}}} \\\\
        Other Fee & {{{OTHER_FEE}}} \\\\
        \\hline
        \\textbf{{Total}} & {{{TOTAL_AMOUNT}}} \\\\
        \\textbf{{Updated Dues}} & {{{REMAINING_DUES}}} \\\\
        \\hline
    \\end{{tabular}}


    \\section{{Thank You !}}

    \\end{{document}}
    """

    # Write LaTeX content to a file
    output_file = "receipts/"+row[3]+ row[2]+ ".tex"
    with open(output_file, "w") as file:
        file.write(latex_content)

    subprocess.run(["pdflatex", output_file])

    print("LaTeX file created successfully.")

    print("Fee receipt generated successfully.")
