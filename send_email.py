import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(row, month, year) :
    # Email configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # or the appropriate port for your SMTP server
    sender_email = 'schoolnovelpublic@gmail.com'
    name = row[0]
    receiver_email = row[1]
    roll = row[2]
    classs = row[3]
    subject = 'Fee Receipt for the month of ' + month + "(" + year + ")"
    body = 'Dear ' + name + ", \nPlease find your fee receipt attached\n" 
    print(body)
    # PDF attachment
    pdf_path = row[3] + row[2] + '.pdf'
    print(pdf_path)

    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach text part
    message.attach(MIMEText(body, 'plain'))

    # Attach PDF part
    with open(pdf_path, 'rb') as pdf_file:
        pdf_attach = MIMEApplication(pdf_file.read(), name='Fee_receipt.pdf')
        message.attach(pdf_attach)

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use this line if your server requires a secure connection

    # Log in to your email account
    server.login(sender_email, 'ajmziwsejblyworh')

    # Send the email
    print(sender_email)
    print(receiver_email)
    # print(message.as_string())
    # sleep(5)
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Disconnect from the server
    server.quit()
