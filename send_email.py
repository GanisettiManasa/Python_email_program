# Email program

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = sender_entry.get()
    sender_password = password_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  
    server.login(sender_email, sender_password)
    
    server.send_message(msg)
    messagebox.showinfo("Success", "Email sent successfully!")
    
    server.quit()

root = tk.Tk()
root.title("Email Chatbot")

root.geometry("600x400")

tk.Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5)
sender_entry = tk.Entry(root, width=50)  
sender_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*", width=50)  
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Receiver Email:").grid(row=2, column=0, padx=10, pady=5)
receiver_entry = tk.Entry(root, width=50)  
receiver_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=3, column=0, padx=10, pady=5)
subject_entry = tk.Entry(root, width=50)  
subject_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Body:").grid(row=4, column=0, padx=10, pady=5)
body_text = tk.Text(root, height=15, width=50)
body_text.grid(row=4, column=1, padx=10, pady=5)

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=5, column=1, pady=10)

root.mainloop()
